import tensorflow as tf
from sklearn.cluster import KMeans

class RMSNorm(tf.keras.layers.Layer):
    def __init__(self, axis=-1, epsilon=1e-5, **kwargs):
        super().__init__(**kwargs)
        self.axis = axis
        self.epsilon = epsilon
    
    def build(self, input_shape):
        self.new_std = self.add_weight(
            name='new_std',
            shape=[input_shape[self.axis], ],
            initializer=tf.constant_initializer(1),
            trainable=True,
            experimental_autocast=False
        )

    def call(self, x):
        x = tf.cast(x, self.new_std.dtype)
        ms = tf.reduce_mean(tf.square(x), axis=-1, keepdims=True)
        norm_inputs = x * tf.math.rsqrt(ms + self.epsilon)
        return norm_inputs * self.new_std
    
    def get_config(self):
        config = {
            'axis': self.axis,
            "epsilon": self.epsilon
        }
        base_config = super(RMSNorm, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))
    

class Identity(tf.keras.layers.Layer):
    def call(self, inputs):
        return tf.nest.map_structure(tf.identity, inputs)


class GumbelSoftmaxLayer(tf.keras.layers.Layer):
    def __init__(
            self,
            initial_temperature=2.0,
            anneal_factor=0.999995,
            min_temperature=0.5,
            layer_index=0,
            **kwargs):
        super(GumbelSoftmaxLayer, self).__init__(**kwargs)
        self.initial_temperature = initial_temperature
        self.use_temperature = self.initial_temperature != 0.0
        self.anneal_factor = anneal_factor
        self.min_temperature = min_temperature

        self.temperature = tf.Variable(
            self.initial_temperature,
            dtype=tf.float32,
            trainable=False,
            name="temperature_{}".format(layer_index))

    def call(self, inputs, training=False):
        if not self.use_temperature or not training:
            indices = tf.argmax(inputs, axis=1)
            encodings = tf.one_hot(indices, tf.shape(inputs)[1])
            return indices, encodings

        gumbel_noise = tf.random.uniform(shape=tf.shape(
            inputs), minval=0, maxval=1, dtype=tf.float32)
        gumbel_noise = -tf.math.log(-tf.math.log(gumbel_noise))

        outputs = tf.argmax(
            tf.nn.softmax(
                (inputs + gumbel_noise) / self.temperature,
                axis=1),
            axis=1)
        encodings = tf.one_hot(outputs, tf.shape(inputs)[1])

        self.update_temperature()
        return outputs, encodings

    def update_temperature(self):
        if not self.use_temperature:
            return

        new_temperature = tf.maximum(
            self.temperature *
            self.anneal_factor,
            self.min_temperature)
        self.temperature.assign(new_temperature)

    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "initial_temperature": self.initial_temperature,
                "anneal_factor": self.anneal_factor,
                "min_temperature": self.min_temperature
            }
        )
        return config


class VectorQuantizer(tf.keras.layers.Layer):
    """
    Args:
        embedding_dim: 埋め込み次元
        num_embeddings: コードブックのサイズ
    """

    def __init__(
            self,
            input_dim,
            embedding_dim,
            codebook_size,
            ema_decay,
            epsilon=1e-6,
            commitment_loss_weight=1.0,
            threshold_ema_dead_code=2.0,
            sample_codebook_temperature=0.0,
            kmeans_init=False,
            use_ema=False,
            layer_index=0,
            **kwargs):
        super().__init__(**kwargs)
        self.embedding_dim = embedding_dim
        self.codebook_size = codebook_size
        self.ema_decay = ema_decay
        self.epsilon = epsilon
        self.commitment_loss_weight = commitment_loss_weight
        self.threshold_ema_dead_code = threshold_ema_dead_code
        self.kmeans_init = kmeans_init
        self.use_ema = use_ema
        self.use_l2norm = not use_ema
        self.layer_index = layer_index

        self.gumbel_softmax = GumbelSoftmaxLayer(
            initial_temperature=sample_codebook_temperature,
            layer_index=layer_index,
            dtype=tf.float32)
        
        self.projection_in = tf.keras.layers.Dense(
            embedding_dim,
            dtype=tf.float32) if input_dim != embedding_dim else Identity(
            dtype=tf.float32)
        self.projection_out = tf.keras.layers.Dense(
            input_dim,
            dtype=tf.float32) if input_dim != embedding_dim else Identity(
            dtype=tf.float32)

    def build(self, input_shape):
        self.embeddings = self.add_weight(
            name="embeddings_{}".format(self.layer_index),
            shape=(self.embedding_dim, self.codebook_size),
            dtype=tf.float32,
            initializer=tf.keras.initializers.random_normal(),
            trainable=self.use_l2norm)
        self.ema_cluster_size = self.add_weight(
            name="ema_cluster_size_{}".format(self.layer_index),
            shape=(self.codebook_size,),
            dtype=tf.float32,
            initializer='zeros',
            trainable=False)
        self.ema_w = self.add_weight(
            name="ema_w_{}".format(self.layer_index),
            shape=(self.embedding_dim, self.codebook_size),
            dtype=tf.float32,
            initializer=tf.initializers.Constant(self.embeddings.numpy()),
            trainable=False)

        self.initialized = tf.Variable(
            False,
            dtype=tf.bool,
            trainable=False,
            name="initialized_{}".format(self.layer_index))

    def init_embeddings(self, inputs):
        if self.initialized:
            return

        kmeans = KMeans(
            n_clusters=self.codebook_size,
            random_state=0).fit(inputs.numpy())

        embedding = tf.convert_to_tensor(
            kmeans.cluster_centers_.T, dtype=tf.float32)
        cluster_size = tf.math.bincount(
            tf.convert_to_tensor(
                kmeans.labels_,
                dtype=tf.int32),
            minlength=self.codebook_size)
        cluster_size = tf.cast(cluster_size, dtype=tf.float32)
        embedding_w = embedding * \
            tf.reshape(cluster_size, [1, -1])

        self.embeddings.assign(embedding)
        self.ema_w.assign(embedding_w)
        self.ema_cluster_size.assign(cluster_size)
        self.initialized.assign(True)

    def decode(self, encoding_indices):
        quantized = tf.nn.embedding_lookup(
            tf.transpose(self.embeddings, [1, 0]),
            encoding_indices)

        quantized = self.projection_out(quantized)
        return quantized

    def expire_codes(self, batch_samples):
        if self.threshold_ema_dead_code <= 0.0:
            return

        dead_codes = self.ema_cluster_size < self.threshold_ema_dead_code

        indices_to_update = tf.where(dead_codes)
        flat_samples = tf.reshape(batch_samples, [-1, tf.shape(batch_samples)[-1]])
        sample_indices = tf.random.shuffle(tf.range(tf.shape(flat_samples)[0]))[:self.codebook_size]
        sampled_vectors = tf.gather(flat_samples, sample_indices)
        vectors_to_update = tf.gather(sampled_vectors, tf.range(tf.minimum(tf.shape(indices_to_update)[0], tf.shape(sampled_vectors)[0])))
        
        updated_embeddings = tf.transpose(self.embeddings)
        updated_embeddings = tf.tensor_scatter_nd_update(updated_embeddings, indices_to_update, vectors_to_update)
        self.embeddings.assign(tf.transpose(updated_embeddings))

        updated_ema_cluster_size = tf.where(
            dead_codes,
            tf.ones_like(
                self.ema_cluster_size) *
            self.threshold_ema_dead_code,
            self.ema_cluster_size)
        self.ema_cluster_size.assign(updated_ema_cluster_size)

        updated_ema_w = tf.where(
            tf.expand_dims(dead_codes, axis=-1),
            updated_embeddings * self.threshold_ema_dead_code,
            tf.transpose(self.ema_w)
        )
        self.ema_w.assign(tf.transpose(updated_ema_w))

    def call(self, inputs, training=False):
        inputs = self.projection_in(inputs)
        flat_inputs = tf.reshape(inputs, [-1, self.embedding_dim])

        if self.kmeans_init:
            tf.py_function(self.init_embeddings, inp=[flat_inputs], Tout=[])

        encoding_indices, encodings = self.get_code_indices(
            flat_inputs, training=training)
        encoding_indices = tf.reshape(encoding_indices, tf.shape(inputs)[:-1])
        quantized = tf.nn.embedding_lookup(
            tf.transpose(self.embeddings, [1, 0]),
            encoding_indices)

        if training and self.trainable and self.use_ema:
            cluster_size = tf.reduce_sum(encodings, 0)
            updated_ema_cluster_size = tf.keras.backend.moving_average_update(
                self.ema_cluster_size, cluster_size, self.ema_decay)

            dw = tf.matmul(
                flat_inputs,
                encodings,
                transpose_a=True)
            updated_ema_w = tf.keras.backend.moving_average_update(
                self.ema_w, dw, self.ema_decay)

            n = tf.reduce_sum(updated_ema_cluster_size)
            updated_ema_cluster_size = (
                (updated_ema_cluster_size + self.epsilon) / (n + self.codebook_size * self.epsilon) * n)
            normalized_updated_ema_w = updated_ema_w / \
                tf.reshape(updated_ema_cluster_size, [1, -1])
            self.embeddings.assign(normalized_updated_ema_w)

            self.expire_codes(inputs)

        commitment_loss = tf.reduce_mean(
            tf.square(tf.stop_gradient(quantized) - inputs))
        
        loss = commitment_loss * self.commitment_loss_weight
        if self.use_l2norm:
            codebook_loss = tf.reduce_mean(
                tf.square(quantized - tf.stop_gradient(inputs))
            )
            loss += codebook_loss
        
        if training:
            quantized = inputs + tf.stop_gradient(quantized - inputs)

        quantized = self.projection_out(quantized)

        return {
            "quantized": quantized,
            "encodings": encodings,
            "encoding_indices": encoding_indices,
            "loss": loss
        }

    def get_code_indices(self, flat_inputs, training=False):
        embeddings = self.embeddings
        if self.use_l2norm:
            flat_inputs = tf.math.l2_normalize(flat_inputs, axis=-1)
            embeddings = tf.math.l2_normalize(embeddings, axis=0)

        similarity = tf.matmul(flat_inputs, embeddings)

        flat_inputs_sum = tf.reduce_sum(
            flat_inputs ** 2,
            axis=1,
            keepdims=True)
        embedding_sum = tf.reduce_sum(
            embeddings ** 2,
            axis=0,
            keepdims=True)

        distances = (flat_inputs_sum - 2 * similarity) + embedding_sum

        encoding_indices, encodings = self.gumbel_softmax(
            -distances, training=training)
        return encoding_indices, encodings

    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "embedding_dim": self.embedding_dim,
                "codebook_size": self.codebook_size,
                "ema_decay": self.ema_decay,
                "epsilon": self.epsilon,
                "threshold_ema_dead_code": self.threshold_ema_dead_code,
                "kmeans_init": self.kmeans_init,
                "layer_index": self.layer_index
            }
        )
        return config


class ResidualVQ(tf.keras.layers.Layer):
    def __init__(
            self,
            input_dim,
            codebook_size,
            embedding_dim,
            num_quantizers,
            ema_decay,
            threshold_ema_dead_code,
            commitment_loss_weight,
            sample_codebook_temperature=0,
            kmeans_init=False,
            use_ema=True,
            **kwargs):
        super().__init__(**kwargs)
        self.codebook_size = codebook_size
        self.embedding_dim = embedding_dim
        self.num_quantizers = num_quantizers
        self.commitment_loss_weight = commitment_loss_weight
        self.vq_layers = [
            VectorQuantizer(
                input_dim=input_dim,
                embedding_dim=embedding_dim,
                codebook_size=codebook_size,
                ema_decay=ema_decay,
                threshold_ema_dead_code=threshold_ema_dead_code,
                commitment_loss_weight=commitment_loss_weight,
                sample_codebook_temperature=sample_codebook_temperature,
                kmeans_init=kmeans_init,
                use_ema=use_ema,
                layer_index=i,
                dtype=tf.float32)
            for i in range(num_quantizers)]

    def get_embeddings(self, quantizer_target_layer_num=None):
        if quantizer_target_layer_num is None:
            quantizer_target_layer_num = self.num_quantizers
            
        return [layer.embeddings for layer in self.vq_layers[:quantizer_target_layer_num]]

    def decode(self, encoding_indices, quantizer_target_layer_num=None):
        if quantizer_target_layer_num is None:
            quantizer_target_layer_num = self.num_quantizers

        quantized_out = 0.0
        all_quantized = []
        for i in range(quantizer_target_layer_num):
            vq_layer = self.vq_layers[i]
            indices = tf.cast(encoding_indices[i], dtype=tf.int32)

            quantized = vq_layer.decode(indices)

            all_quantized.append(quantized)
            quantized_out += quantized

        return quantized_out, all_quantized


    def call(self, inputs, training=False, quantizer_target_layer_num=None):
        residual = inputs
        quantized_out = 0.

        losses = []
        all_quantized = []
        encoding_indices = []
        for i, layer in enumerate(self.vq_layers):
            if quantizer_target_layer_num is not None:
                if i >= quantizer_target_layer_num:
                    break
            
            vq_output = layer(residual, training=training)
            residual = residual - vq_output['quantized']
            quantized_out = quantized_out + vq_output['quantized']

            losses.append(vq_output['loss'])
            all_quantized.append(vq_output['quantized'])
            encoding_indices.append(vq_output['encoding_indices'])

        if self.commitment_loss_weight != 0:
            self.add_loss(tf.reduce_sum(losses))
            self.add_metric(
                tf.math.reduce_sum(losses),
                name="residual_vq_commitment")

        return quantized_out, all_quantized, encoding_indices

    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "codebook_size": self.codebook_size,
                "embedding_dim": self.embedding_dim,
                "num_quantizers": self.num_quantizers,
                "commitment_loss_weight": self.commitment_loss_weight
            }
        )
