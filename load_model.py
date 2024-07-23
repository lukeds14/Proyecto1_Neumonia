import tensorflow as tf #Se instala la version TF 2.15.0 porque con la version actual arroja un error
tf.compat.v1.disable_eager_execution()
tf.compat.v1.experimental.output_all_intermediates(True)

def model_fun():
    model = tf.keras.models.load_model('conv_MLP_84.h5')
    if not model.compiled_loss:
        loss = tf.keras.losses.CategoricalCrossentropy(reduction='sum_over_batch_size')
        model.compile(optimizer='adam', loss=loss)
    return model
