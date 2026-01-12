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
    def __init__(self, dataset, y = None):
        if y is None:
            self.X_s = dataset[:, 0]
            self.y_s = dataset[:, 1]
        else:
            self.X_S = dataset
            self.y_s = y
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
    
    def get_binary_confusion(self, ground_truth, predicted):
        conf = {'TN': 0, 'FN': 0, 'FP': 0, 'TP': 0}
        for gt, p in zip(ground_truth, predicted):
            if p == 0 and gt == 0:
                conf['TN'] += 1
            elif p == 0 and gt == 1:
                conf['FN'] += 1
            elif p == 1 and gt == 1:
                conf['TP'] += 1
            else:
                conf['FP'] += 1
        return conf
    
    def binary_precision(self, conf_M):
        """
        Of the ones classified to positive, how many were actually positive?
        """
        return conf_M['TP'] / (conf_M['TP'] + conf_M['FP'])
    
    def binary_recall(self, conf_M):
        """
        also: sensitivity, true positive rate
        Of the actually positive samples, how many were classified to positive?
        """
        return conf_M['TP'] / (conf_M['TP'] + conf_M['FN'])
    
    def binary_specificity(self, conf_M):
        """
        Of the actually negative samples, how many were classified to negative?
        (same as recall, but for the negative class)
        """
        return conf_M['TN'] / (conf_M['TN'] + conf_M['FP'])
    
    def binary_MCC(self, conf_M):
        """
        Matthew's Correlation Coefficient (MCC) or the 'phi coefficient' is a correlation
        based metric that measures the quality of binary classification even with
        imbalanced classes
        """
        nom = conf_M['TP'] * conf_M['TN'] - conf_M['FP'] * conf_M['FN']
        denom = (conf_M['TP'] +  conf_M['FP']) * (conf_M['TP'] +  conf_M['FN']) * (conf_M['TN'] +  conf_M['FP']) * (conf_M['TN'] +  conf_M['FN'])
        return nom / sqrt(denom)
    
    def binary_F1(self, conf_M):
        """
        harmonic mean of precision and recall
        """
        p = self.binary_precision(conf_M)
        r = self.binary_recall(conf_M)
        return 2 * p * r / (p + r)
    
    def print_binary_metrics(self, conf_M):
        print(f"Precision:\t{self.binary_precision(conf_M)}\nRecall:\t\t{self.binary_recall(conf_M)}")
        print(f"F1:\t\t{self.binary_F1(conf_M)}\nSpecificity:\t{self.binary_specificity(conf_M)}")
        print(f"MCC:\t\t{self.binary_MCC(conf_M)}")

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