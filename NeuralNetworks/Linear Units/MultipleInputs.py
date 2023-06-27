# Multiple Inputs
import numpy as np
import pandas as pd

class LinearUnit:
    def __init__(self, input_nn):
        self.input_nn = input_nn
        self.weight = []
        self.bias = np.random.randint(1, 100)
        self.create_weights()

    def create_weights(self):
        for i in range(len(self.input_nn[0])):
            self.weight.append(np.random.rand(1))

    def print_me(self):
        data_frame = pd.DataFrame({'First Input': [self.input_nn[0][0], self.weight[0], self.bias], 'Second Input': [self.input_nn[0][1], self.weight[1], self.bias], 'Third Input': [self.input_nn[0][2], self.weight[2], self.bias]}, index=['Input', 'Weight', 'Bias'])
        print(data_frame)

    def predict(self):
        y = []

        #Sum all inputs with each of their weights and add them up to y

        for i in range(len(self.input_nn[0])):
            y.append(self.input_nn[0][i] * self.weight[i])
        
        #Sum them up and add the bias
        return np.sum(y) + self.bias


inputs = np.floor(np.random.rand(1,3) * 3)

linear_unit = LinearUnit(inputs)

#linear_unit.print_me()

predict = linear_unit.predict()

print(predict)