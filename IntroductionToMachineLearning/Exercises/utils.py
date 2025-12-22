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
        
        self.weights = np.linalg.inv(self.design_matrix) @ self.y_s
        return self.weights
    
    def predict(self, new_X_s, degree = None):
        assert self.design_matrix is not None or degree is not None
        if degree is not None:
            self.get_weights(degree)
        
        l = [np.ones(len(new_X_s))] + [new_X_s ** i for i in range(1, self.degree+1)]
        l.reverse()
        return np.array(l).T @ self.weights
        