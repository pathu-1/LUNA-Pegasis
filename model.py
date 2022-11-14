import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array

style_transfer_model = hub.load("https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2")


def style_transfer(content_image_path, style_image_path):
    content_ = load_img(content_image_path)
    style_ = load_img(style_image_path, target_size=(256, 256))

    content_ = img_to_array(content_)
    style_ = img_to_array(style_)

    content_ = tf.expand_dims(content_, axis=0)/255.
    style_ = tf.expand_dims(style_, axis=0)/255.

    output_ = style_transfer_model(content_, style_)
    stylized_image = output_[0]

    return Image.fromarray(np.uint8(stylized_image[0]*255))






