# -*- coding: utf-8 -*-

"""
Author: Juan Camilo Florez R. <florez87@gmail.com>
"""

from bussiness.DecisionTrees import DecisionTree
from bussiness.Utilities import Utilities
import numpy
import os

class AppController(object):
    """
    Manages the information flow and actions between the GUI and the bussiness layer.
    
    Attributes
    ----------
    dataset: Dataframe
        The current dataset of features and labels.
    
    classes: array of shape = [number_classes] 
        The list of arrays of current class labels (multi-output problem).

    path_caldas: string
        The location of the persistence directory for Caldas database.
        
    path_adni: string
        The location of the persistence directory for ADNI database.
        
    classifier_caldas: DecisionTree
        The model for training and predicting over Caldas database.
        
    classifier_adni: DecisionTree
        The model for training and predicting over ADNI database.
    """
    def __init__(self):
        self.dataset = None
        self.classes = None
        self.path_caldas = 'persistence/Caldas/'
        self.path_adni = 'persistence/ADNI/'
        self.classifier_caldas = DecisionTree('Caldas')
        self.classifier_adni = DecisionTree('ADNI')
        self.loadCaldas()
        self.loadADNI()
        
    def train(self, path, database):
        """
        Trains an specific model with the features and labels read from a file.
        
        Parameters
        ----------
        path: string
             The location of the file with the features and labels for training.
            
        database: string
            The name of the database.
        
        Return
        ----------
        succesful: boolean
            Wether the training of the model was succesful.
        """
        if not Utilities.checkFile(path, database):
            return False
        else:
            dataframe = Utilities.readCSV(path)
            labels = dataframe['Diagnosis'].values
            classes, ids = Utilities.getClasses(labels)
            if database == 'Caldas':
                features = dataframe[list(['CDR', 'MMSE', 'MoCA', 'GDS'])].values
                self.classifier_caldas.train(features, labels)
                self.classifier_caldas.trained = True
                self.classifier_caldas.classes = classes
            else:
                features = dataframe[list(['CDR', 'MMSE', 'Age', 'Education'])].values
                self.classifier_adni.train(features, labels)
                self.classifier_adni.trained = True
                self.classifier_adni.classes = classes
            return True
    
    def predict(self, cdr, mmse, moca, gds, age, education, database):
        """
        Predict label and class probabilities of the input sample (features).
        
        Parameters
        ----------
        cdr: float
            The Clinical Dementia Rating of the person.
        
        mmse: float
            The Mini–Mental State Examination score of the person.
            
        moca: float
            the Montreal Cognitive Assessment score of the person.
            
        gds: float
            The Global Deterioration Scale of the person.
            
        age: int
            The age of the person in years.
            
        education: int
            The amount of education years of the person.
            
        database: string
            The name of the database.
        
        Return
        ----------
        succesful: boolean
            Wether the prediction of the model was succesful.
        
        diagnosis: array of shape = [1]
            The predicted class for the input sample.
            
        probabilities: array of shape = [1, number_classes]
            The class probabilities for the input sample in percentage.
            
        classes: array of shape = [number_classes] 
            The list of arrays of class labels (multi-output problem).
        """
        features = []
        features.append(float(cdr))
        features.append(mmse)
        if database == 'Caldas':
            features.append(moca)
            features.append(gds)
            if self.classifier_caldas.trained:
                features = numpy.reshape(features, (1, -1))
                diagnosis, prediction = self.classifier_caldas.predict(features)
                classes = self.classifier_caldas.classes
            else:
                return False, None, None, None
        else:
            features.append(age)
            features.append(education)
            if self.classifier_adni.trained:
                features = numpy.reshape(features, (1, -1))
                diagnosis, prediction = self.classifier_adni.predict(features)
                classes = self.classifier_adni.classes
            else:
                return False, None, None, None
        return True, diagnosis, prediction * 100, classes
        
    def save(self):
        """
        Saves the models if they are already trained.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        if self.classifier_caldas.trained:
            self.classifier_caldas.save(self.path_caldas)
        if self.classifier_adni.trained:
            self.classifier_adni.save(self.path_adni)
    
    def loadCaldas(self):
        """
        Loads the model for Caldas database if it's persisted in path_caldas
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        for dirpath, dirnames, files in os.walk(self.path_caldas):
            if files:
                self.classifier_caldas.load(self.path_caldas)
                self.classifier_caldas.trained = True
                
    def loadADNI(self):
        """
        Loads the model for ADNI database if it's persisted in path_adni
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        for dirpath, dirnames, files in os.walk(self.path_adni):
            if files:
                self.classifier_adni.load(self.path_adni)
                self.classifier_adni.trained = True
                
    def validate(self, path, number_folds, database):
        """
        Compute a model's performance metrics based on k-fold cross-validation technique.
        
        Parameters
        ----------
        path: string
            The location of the file with the features and labels for validation.
            
        number_folds: int
            The amount of folds for the k-fold cross-validation.
            
        database: string
            The name of the database.
        
        Return
        ----------
        checked: boolean
            Whether the columns/classes in the file correspond to the ones associated with the database.  
        
        validated: boolean
            Wether the validation of the model was succesful.
            
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
        if not Utilities.checkFile(path, database):
            return False, True, None, None, None, None, None
        else:
            dataframe = Utilities.readCSV(path)
            labels = dataframe['Diagnosis'].values
            if database == 'Caldas':
                if self.classifier_caldas.trained:
                    features = dataframe[list(['CDR', 'MMSE', 'MoCA', 'GDS'])].values
                    accuracy, precision, sensitivity, specificity, kappa = self.classifier_caldas.validate(features, labels, number_folds)
                else:
                    return True, False, None, None, None, None, None
            else:
                if self.classifier_adni.trained:
                    features = dataframe[list(['CDR', 'MMSE', 'Age', 'Education'])].values
                    accuracy, precision, sensitivity, specificity, kappa = self.classifier_adni.validate(features, labels, number_folds)
                else:
                    return True, False, None, None, None, None, None
            return True, True, accuracy, precision, sensitivity, specificity, kappa
        
    def isTrained(self):
        if self.classifier_caldas.trained or self.classifier_adni.trained:
            return True
        else:
            return False

