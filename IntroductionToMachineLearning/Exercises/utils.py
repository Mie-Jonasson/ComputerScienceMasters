from typing import List
from math import sqrt, degrees
import numpy as np

class ListVector:
    def __init__(self, v: List):
        self.vector = v
    
    def length(self):
        return sqrt(sum([i**2 for i in self.vector]))
    
    def dot(self, other):
        assert len(self.vector) == len(other.vector)
        return sum([i * j for i, j in zip(self.vector, other.vector)])

class NumpyVector:
    def __init__(self, v: List):
        self.vector = np.array(v)
    
    def length(self):
        return sqrt(np.sum(self.vector**2))
    
    def angle(self, other):
        cos_angle = np.dot(self.vector, other.vector) / (self.length() * other.length())
        angle = np.arccos(cos_angle)
        return (angle, degrees(angle))
    
    def distance(self, other):
        return NumpyVector(self.vector - other.vector).length()

class processDataset:
    def __init__(self, dataset):
        self.X_s = dataset[:, 0]
        self.y_s = dataset[:, 1]
        self.degree = None
        self.design_matrix = None
        self.projection_matrix = None
        self.weights = None
    
    def get_design_matrix(self, degree):
        self.degree = degree
        l = [np.ones(len(self.X_s))] + [self.X_s ** i for i in range(1, degree+1)]
        l.reverse()
        self.design_matrix = np.array(l).T
        return self.design_matrix
    
    def get_weights(self, degree = None):
        assert self.design_matrix is not None or degree is not None
        if degree is not None:
            self.get_design_matrix(degree)
        
        self.projection_matrix = np.linalg.inv(self.design_matrix.T @ self.design_matrix) @ self.design_matrix.T
        self.weights = self.projection_matrix @ self.y_s
        return self.weights
    
    def predict(self, new_X_s, degree = None):
        assert self.design_matrix is not None or degree is not None
        if degree is not None:
            self.get_weights(degree)
        
        l = [np.ones(len(new_X_s))] + [new_X_s ** i for i in range(1, self.degree+1)]
        l.reverse()
        return np.array(l).T @ self.weights

class Eval:
    def __init__(self):
        pass

    def mse(self, ground_truth, predictions):
        return ((ground_truth - predictions)**2).mean()
    
    def rmse(self, ground_truth, predictions):
        return sqrt(self.mse(ground_truth, predictions))
    
    def accuracy(self, ground_truth, predictions):
        return sum(ground_truth == predictions) / len(ground_truth)

class LogisticRegression:
    def __init__(self):
        pass

    def sigmoid(self, z):
        return 1 / (1 + e ** (-z))
    
    def linear_sigmoid(self, x, b, w) :  # sigmoid function
        """
        :param x: 1D array of the (single) input-feature values.
        :param b: The bias parameter of the model.
        :param W: The weight parameter of the model.
        
        :return (float): output values of the sigmoid function. 
        """
        z = x * w + b
        return self.sigmoid(z)
    
    def linear_decision_boundary(self, b, w):
        return -b / w
    
    def linear_predict(self, x, w):
        """
        :param x: 1D array of the (single) input-feature values.
        :param w: The list of the model parameters, [bias, weight]. 
        
        :return: Boolean array same size as x, where a True values signifies class2, and False signifies class1
        """
        sig = self.linear_sigmoid(x, w[0], w[1])
        return np.array([bool(round(x, 0)) for x in sig])
    
    def sigmoid2D(self, X, params) :  # sigmoid function
        """
        :param X: tuple of input features (x,y).
        :param parametes: The list of the model parameters, [bias, weight1, weight2]. 
        :return: output values of the sigmoid function. 
        """
        # Write solutions here
        z = X[0] * params[1] + X[1] * params[2] + params[0]
        return self.sigmoid(z)
    
    def predict2D(self, X, params):
        """
        :param x: tuple of 1D arrays of the input-feature values.
        :param params: The list of the model parameters, [bias, weight1, weight2]. 
        
        :return: Boolean array same size as x, where a True values signifies class2, and False signifies class1
        """
        sig = self.sigmoid2D(X, params)
        return np.array([bool(round(x, 0)) for x in sig])