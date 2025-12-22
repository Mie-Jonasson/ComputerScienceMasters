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
