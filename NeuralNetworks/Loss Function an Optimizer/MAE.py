# MAE = abs(y_pred - y_target) -> the less the better
# ReLu = max(0, (wx1 + wx + wxn)) + bias 
# Linear Unit = Y = wx + b

# ANN that uses ReLu as activation function in the hidden layers, it's linear in the output layer, and uses MAE as loss function

import numpy as np
import os
import time

class ANN:
    def __init__(self, inputs, hidden_layers=3, units=[4,6,3], training_cycle=10, target=102):
        if(hidden_layers != len(units)):
            raise ValueError('Numbers of Units does not match Hidden Layers')
        self.hidden_layers = hidden_layers
        self.units = units
        self.inputs = inputs
        self.training_cycle = training_cycle
        self.target = target

    def predict(self):
        Units = []
        Layers = []
        Y = []

        Training_cycle = []
        B = 10
        W = 5

        Bias = np.random.randint(1, B)

        print("_____Training Model_____")
        for training in range(self.training_cycle):
            os.system("clear")
            count = "#" * training
            print("Training: " + count)
            time.sleep(0.4)
            for layer in range(self.hidden_layers):
                for i in range(self.units[layer]):
                    for load in self.inputs:
                        weight = np.random.rand(1) * W
                        Y.append(load * weight)
                    Units.append(max(0, sum(Y) + Bias))
                    Y = []
                self.inputs = Units
                Layers.append(Units)
                Units = []
            

            Training_cycle.append(abs(self.target - (sum(Layers[-1]) + Bias)))
            Y = []
            if Training_cycle[-1] > self.target:
                W -= 0.6
                B -= 0.1

            P = Training_cycle[-1]
            Result = 0
            if type(P) != type(1):
                Result = P[-1]
            else:
                Result = P
        
        print(f"Training Y: {str(Result)} \nTarget: {str(self.target)} \nAccuracy: {np.round(Result / self.target * 100)}%")


if __name__ == '__main__':
    inputs = np.round(np.random.rand(3) * 8)
    neural_network = ANN(inputs=inputs)
    neural_network.predict()