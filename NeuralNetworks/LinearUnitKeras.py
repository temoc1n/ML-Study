import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras import layers, Sequential

# Dense Layer = NN's organize their neurons into layers. When we collect together linear units having a common set of inputs we get a dense layer.
# Units = outputs
# Input_Shape = inputs

model = Sequential(layers.Dense(units= 1, input_shape=[1]))

x = tf.linspace(-1.0, 1.0, 100)

y = model.predict(x)

weights = model.weights



print(y)


