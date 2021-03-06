import numpy as np
from numpy.core.numeric import identity
from numpy.lib.function_base import append, cov
import pandas as pd

############################################################################
# DO NOT MODIFY CODES ABOVE 
# DO NOT CHANGE THE INPUT AND OUTPUT FORMAT
############################################################################

###### Part 1.1 ######
def mean_square_error(w, X, y):
    """
    Compute the mean square error of a model parameter w on a test set X and y.
    Inputs:
    - X: A numpy array of shape (num_samples, D) containing test features
    - y: A numpy array of shape (num_samples, ) containing test labels
    - w: a numpy array of shape (D, )
    Returns:
    - err: the mean square error
    """
    #####################################################
    # TODO 1: Fill in your code here                    #
    #####################################################
    err = 0

    for n in range(len(X)):
      err += np.square((np.transpose(X[n]) @ w) - y[n]) / len(X)

    return err

###### Part 1.2 ######
def linear_regression_noreg(X, y):
  """
  Compute the weight parameter given X and y.
  Inputs:
  - X: A numpy array of shape (num_samples, D) containing features
  - y: A numpy array of shape (num_samples, ) containing labels
  Returns:
  - w: a numpy array of shape (D, )
  """
  #####################################################
  #	TODO 2: Fill in your code here                    #
  #####################################################		
  X_T = np.transpose(X)
  w = np.linalg.inv(X_T @ X) @ X_T @ y

  return w


###### Part 1.3 ######
def regularized_linear_regression(X, y, lambd):
    """
    Compute the weight parameter given X, y and lambda.
    Inputs:
    - X: A numpy array of shape (num_samples, D) containing features
    - y: A numpy array of shape (num_samples, ) containing labels
    - lambd: a float number specifying the regularization parameter
    Returns:
    - w: a numpy array of shape (D, )
    """
  #####################################################
  # TODO 4: Fill in your code here                    #
  #####################################################		
    X_T = np.transpose(X)
    covariance = X_T @ X
    reg = lambd * np.identity(len(covariance))
    w = np.linalg.inv(covariance + reg) @ X_T @ y

    return w

###### Part 1.4 ######
def tune_lambda(Xtrain, ytrain, Xval, yval):
    """
    Find the best lambda value.
    Inputs:
    - Xtrain: A numpy array of shape (num_training_samples, D) containing training features
    - ytrain: A numpy array of shape (num_training_samples, ) containing training labels
    - Xval: A numpy array of shape (num_val_samples, D) containing validation features
    - yval: A numpy array of shape (num_val_samples, ) containing validation labels
    Returns:
    - bestlambda: the best lambda you find among 2^{-14}, 2^{-13}, ..., 2^{-1}, 1.
    """
    #####################################################
    # TODO 5: Fill in your code here                    #
    #####################################################		
    lambdas = [1 / np.power(2, 15 - x) for x in range(1, 16)]
    min_mse = np.inf
    bestlambda = lambdas[0]
    
    for lambd in lambdas:
      w = regularized_linear_regression(Xtrain, ytrain, lambd)
      mse = mean_square_error(w, Xval, yval)
      if mse < min_mse:
        min_mse = mse
        bestlambda = lambd

    return bestlambda
    

###### Part 1.6 ######
def mapping_data(X, p):
    """
    Augment the data to [X, X^2, ..., X^p]
    Inputs:
    - X: A numpy array of shape (num_training_samples, D) containing training features
    - p: An integer that indicates the degree of the polynomial regression
    Returns:
    - X: The augmented dataset. You might find np.insert useful.
    """
    #####################################################
    # TODO 6: Fill in your code here                    #
    #####################################################		
    mapped_X = X

    for k in range(2, p + 1):
      X_power = [[np.power(x[i], k) for i in range(len(x))] for x in X]
      mapped_X = np.insert(mapped_X, len(mapped_X[0]), np.transpose(X_power), axis = 1)
   
    return mapped_X

"""
NO MODIFICATIONS below this line.
You should only write your code in the above functions.
"""

