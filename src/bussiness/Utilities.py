# -*- coding: utf-8 -*-

"""
Author: Juan Camilo Florez R. <florez87@gmail.com>
"""

import pandas
import numpy
from sklearn.cross_validation import StratifiedKFold

class Utilities(object):
    """
    Tools to check read, check, validate and transform input.
    """
    @staticmethod
    def readCSV(path):
        """
        Read a csv file with pandas library.
        
        Parameters
        ----------
        path: string
            The location of the file to read.
        
        Return
        ----------
        dataset: DataFrame
            The data read from the CSV.
        """
        return pandas.read_csv(path)
                        
    @staticmethod
    def getClasses(labels):
        """
        Get unique values from a column of labels.
        
        Parameters
        ----------
        labels: array-like of shape = [number_samples] or [number_samples, number_outputs]
            The target values (class labels in classification).
        
        Return
        ----------
        classes: ndarray
            The sorted unique labels
        
        ids: ndarray
            The indices of the first occurrences of the unique values in the original array.
        """
        uniques, ids = numpy.unique(labels, return_inverse=True)
        return uniques, ids
        
    @staticmethod
    def getFolds(labels, number_folds):
        """
        Provides train/test indices to split data in train test sets.
        
        Parameters
        ----------
        labels: array-like of shape = [number_samples]
            The target values (class labels in classification).
            
        number_folds: int
            The amount of folds for the k-fold cross-validation.
        
        Return
        ----------
        folds: StratifiedKFold
            the train/test indices of the splitted data. 
        """
        return StratifiedKFold(y=labels, n_folds=number_folds, shuffle=True)

    @staticmethod
    def checkFile(path, database):
        """
        Checks if columns/classes in a file correspond to the ones associated with the database.
        
        Parameters
        ----------
        path: string
            The location of the file to check.
            
        database: string 
            The name of the database.
        
        Return
        ----------
        valid: boolean
            Whether the columns/classes in the file correspond to the ones associated with the database. 
        """
        dataframe = Utilities.readCSV(path)
        labels = dataframe['Diagnosis'].values
        classes, ids = Utilities.getClasses(labels)
        if set(classes) == set(['Sane', 'Mild', 'Serious']):
            headers = list(dataframe)
            if database == 'Caldas':
                if set(headers) == set(['CDR', 'MMSE', 'MoCA', 'GDS', 'Diagnosis']):
                    return True
                else:
                    return False
            else:
                if set(headers) == set(['CDR', 'MMSE', 'Age', 'Education', 'Diagnosis']):
                    return True
                else:
                    return False
        else:
            return False