from tensorflow import keras
from tensorflow.python.keras import Sequential, layers
import numpy as np
#relu = max(0, (wx1 + wx2 + 2xn) + b)

module = Sequential([
    layers.Dense(units=3, input_shape=[11], activation='relu'),
    layers.Dense(units=7, activation='relu'),
    layers.Dense(units=5, activation='relu'),
    layers.Dense(units=1)
])


module.compile(optimizer='adam',loss='mae')

X = np.random.rand(1, 11)

y = np.array([[1]])

history = module.fit(X, y, epochs=200, batch_size=36)

Y = module.predict(X)

print(Y)
print(y)