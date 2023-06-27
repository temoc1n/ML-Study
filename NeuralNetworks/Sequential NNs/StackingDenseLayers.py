#ANN nonelinear with stacked dense layers

import numpy as np
import pandas as pd

class ANN:
    def __init__(self, inputs, layers=2, units=[4,3]):
        self.inputs = inputs
        self.layers = layers
        self.units = units


    def predict(self):
        # Y = X * W + B

        Units = []
        Layers = []

        bias = np.random.randint(1, 10)

        for layer in range(self.layers):
            for units in range(self.units[layer]):
                Loads = []
                for i in range(len(self.inputs)):
                    weight = np.random.rand(1)[0] * 10
                    Loads.append([self.inputs[i] * weight])
                #Returns the value passing by a ReLu Activation
                Units.append(max(0, sum(Loads[len(Loads) - 1]) + bias))
            Layers.append(Units)
            self.inputs = Units
            Units = []

        #Output Linear Layer

        Y = np.round(sum(Layers[-1]) + bias)
        
        return Y




if __name__ == '__main__':

    inputs = [np.random.randint(1,10) for _ in range(2)]

    ann = ANN(inputs=inputs)

    prediction = ann.predict()

    print(prediction)