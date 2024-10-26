 
# File: backend/app/models/neural_network.py

import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.weights_ih = np.random.randn(self.hidden_size, self.input_size)
        self.bias_h = np.zeros((self.hidden_size, 1))
        self.weights_ho = np.random.randn(self.output_size, self.hidden_size)
        self.bias_o = np.zeros((self.output_size, 1))
        
    def forward(self, X):
        self.hidden = np.dot(self.weights_ih, X) + self.bias_h
        self.hidden_output = self.sigmoid(self.hidden)
        self.output = np.dot(self.weights_ho, self.hidden_output) + self.bias_o
        self.predictions = self.sigmoid(self.output)
        return self.predictions
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))