# Linear Units -> Is a single neuron :P -> y = weight * input + bias or y = wx + b
import numpy as np


class LinearUnit:
    def __init__(self, training_life):
        self.bias = np.random.randint(1,100)
        self.weight = np.random.rand(1)[0] * 10
        self.training_life = training_life
        self.target = 102.5

    def predict(self, input_nn):
        
        training_res = []

        for i in range(self.training_life):
            print(f"Training ± Bias {self.bias} | Weight {self.weight} | Input {input_nn}")
            training_res.append(self.weight * input_nn + self.bias)
            self.weight += np.random.randint(1, self.training_life)
            self.bias += np.random.rand(1)[0] * self.training_life
        
        accurate_pred = self.target

        for j in training_res:
            if j <= self.target:
                if j == self.target:
                    return j
                else:
                    if (self.target - j) > accurate_pred:
                        accurate_pred = self.target - i

        return accurate_pred
    



neuron = LinearUnit(100)

pred = neuron.predict(5)

print(pred)