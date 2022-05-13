import tensorflow as tf
from tensorflow import keras
from keras.models import load_model


class Model:

    def __init__(self):
        self.model = load_model("./models/model.h5")

    def decode_test(self, filename):
        img = tf.io.read_file(filename)
        img = tf.io.decode_jpeg(img, channels=3)
        img = tf.cast(img, tf.float32)
        return img

    def load_test_ds(self, filename):
        imgs = ['data/' + filename]
        ds = tf.data.Dataset.from_tensor_slices(imgs)
        ds = ds.map(self.decode_test)
        ds = ds.batch(64)
        return ds

    def make_predictions(self, filename):
        result = self.model.predict(self.load_test_ds(filename))
        return result
