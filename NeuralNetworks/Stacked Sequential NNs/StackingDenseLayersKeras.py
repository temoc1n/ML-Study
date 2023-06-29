from tensorflow import keras
import numpy as np
from tensorflow.python.keras import layers, Sequential




model = Sequential([
    layers.Dense(units=4, activation='relu', input_shape=[11]), #Input Layer and First Hidden Layer
    layers.Dense(units=3, activation='relu'),   # Second Hidden Layer
    layers.Dense(units=1), # Output Layer
])

X = np.random.rand(1, 11)

Y = model.predict(X)

print(Y)