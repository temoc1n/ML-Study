import numpy as np
import pandas as pd

class ReLu:
    def __init__(self, input_nn):
        self.input_nn = input_nn
        self.bias = np.random.randint(1, 10)
        self.weight = np.random.rand(4) * 10

    def print_w_b(self):
        data_frame = pd.DataFrame({'Inputs': self.input_nn, 'Weights': self.weight, 'Bias': self.bias}, index=['First Input', 'Second Input', 'Third Input', 'Forth Input'])
        return data_frame
    
    def predict(self):
        
        y = []

        #Calculate w*xn + b
        for i in range(len(self.input_nn)):
            y.append(self.input_nn[i] * self.weight[i] + self.bias)
        
        # Use a ReLu activation
        return max(0, sum(y))
    


if __name__ == '__main__':

    inputs = np.random.rand(4) * 50


    relu = ReLu(inputs)
    prediction = relu.predict()

    print(prediction)

    data_frame = relu.print_w_b()

    print(data_frame)
