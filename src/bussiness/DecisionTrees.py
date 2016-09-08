# -*- coding: utf-8 -*-

"""
Author: Juan Camilo Florez R. <florez87@gmail.com>
"""

from bussiness.Classifiers import Classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import cross_val_predict
import numpy

class DecisionTree(Classifier):
    """
    A decision tree classifier based on scikit-learn DecisionTreeClassifier.
    
    Parameters
    ----------
    database: string 
        The name of the database associated with the classifier.
        
    Attributes
    ----------
    trained: boolean
        Wether the model is already trained with any data.
        
    model: DecisionTreeClassifier
        The decision tree classifier from scikit-learn framework.
        
    classes: array of shape = [number_classes] 
        The list of arrays of class labels (multi-output problem).
    """
    def __init__(self, database):
        self.database = database
        self.trained = False
        self.model = DecisionTreeClassifier()
        self.classes = None
        
    def train(self, features, labels):
        """
        Train the model itself with a data set (features, labels).
        
        Parameters
        ----------
        features: array-like of shape = [number_samples, number_features]
            The training input samples.
            
        labels: array-like of shape = [number_samples] or [number_samples, number_outputs]
            The target values (class labels in classification).
            
        Return
        ----------
        None
        """
        self.model.fit(features, labels)
        
    def predict(self, features):
        """
        Predict label and class probabilities of the input sample (features).
        
        Parameters
        ----------
        features: array-like of shape = [1, number_features]
            The input sample.
        
        Return
        ----------
        label: array of shape = [1]
            The predicted class for the input sample.
            
        probabilities: array of shape = [1, number_classes]
            The class probabilities for the input sample. The order of the
            classes corresponds to that in the attribute `classes`.
        """
        return self.model.predict(features), self.model.predict_proba(features)
        
    def save(self, path):
        """
        Persist the model itself and it's classes with joblib and pickle.
        
        Parameters
        ----------
        path: string
            The location of the persistence directory where model and classes will be stored.
        
        Return
        ----------
        None
        """
        joblib.dump(self.model, path + 'tree.pkl')
        joblib.dump(self.classes, path + 'classes.pkl')
    
    def load(self, path):
        """
        Load a model and it's classes with joblib and pickle.
        
        Parameters
        ----------
        path: string
            The location of the persistence directory from which model and classes will be loaded.
        
        Returns
        ----------
        None
        """
        self.model = joblib.load(path + 'tree.pkl')
        self.classes = joblib.load(path + 'classes.pkl')
        
    def validate(self, features, labels, number_folds):
        """
        Compute a model's performance metrics based on k-fold cross-validation technique.
        
        Parameters
        ----------
        features: array-like of shape = [number_samples, number_features]
            The validation input samples.
            
        labels: array-like of shape = [number_samples] or [number_samples, number_outputs]
            The target values (class labels in classification).
            
        number_folds: int
            The amount of folds for the k-fold cross-validation.
            If 0 compute metrics withput folds.
            If > 0 compute metrics with n folds, n=number_folds.
        
        Return
        ----------
        accuracy: float
            The accuracy of the model based on it's confusion matrix.
            
        precision: float
            The precision of the model based on it's confusion matrix.
            
        sensitivity: float
            The sensitivity of the model based on it's confusion matrix.
            
        specificity: float
            The specificity of the model based on it's confusion matrix.
            
        kappa: float
            The Cohen's Kappa of the model based on it's confusion matrix.
        """
        if number_folds == 0:
            predictions = self.model.predict(features)
        else:
            predictions = cross_val_predict(self.model, features, labels, cv = number_folds)
        matrix = confusion_matrix(labels, predictions)
        sum_columns = numpy.sum(matrix, 0)
        sum_rows = numpy.sum(matrix, 1)
        diagonal_sum = numpy.trace(matrix)
        total_sum = numpy.sum(sum_rows)
        accuracy = diagonal_sum / total_sum
        temp_precision = []
        temp_sensitivity = []
        temp_specificity = []
        for i in range(len(matrix)):
            temp_precision.append(matrix[i][i] / sum_columns[i])
            temp_sensitivity.append(matrix[i][i] / sum_rows[i])
            temp_reduced_sum = total_sum - sum_rows[i] - sum_columns[i] + matrix[i][i]
            temp_specificity.append(temp_reduced_sum / (temp_reduced_sum + sum_columns[i] - matrix[i][i]))
        precision = sum(temp_precision * sum_rows) / total_sum
        sensitivity = sum(temp_sensitivity * sum_rows) / total_sum
        specificity = sum(temp_specificity * sum_rows) / total_sum
        kappa_sum = sum(sum_rows * sum_columns)
        kappa_numerator = (total_sum * diagonal_sum) - kappa_sum
        kappa_denominator =  (total_sum * total_sum) - kappa_sum
        kappa = kappa_numerator / kappa_denominator
        return accuracy, precision, sensitivity, specificity, kappa       