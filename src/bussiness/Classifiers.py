# -*- coding: utf-8 -*-

"""
Author: Juan Camilo Florez R. <florez87@gmail.com>
"""

import abc

class Classifier(metaclass=abc.ABCMeta):
    """
    Base class for application classifiers
    
    Warning: This class should not be used directly.
    Use derived classes instead.
    """

    @abc.abstractmethod
    def train(features, labels):
        return
        
    @abc.abstractmethod
    def predict(features):
        return
        
    @abc.abstractmethod
    def save(path):
        return
        
    @abc.abstractmethod
    def load(path):
        return
        
    @abc.abstractmethod
    def validate(path, number_folds):
        return

