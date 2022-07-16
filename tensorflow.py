import tensorflow as tf
import numpy as np

# Convert Celsius -> Fahrenheit using an artificial neural network

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype = float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype= float)

from tensorflow import keras

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

