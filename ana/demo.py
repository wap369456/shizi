from statsmodels.tsa.stattools import adfuller
from sklearn.linear_model import LinearRegression
from keras.models import  Sequential
from gensim import sklearn_api
import numpy as np
a = np.array([1, 2, 3])
print(a)
a = np.array([[1, 2], [3, 4]])
print(a)
dt = np.dtype(np.int32)
print(dt)
dt = np.dtype('i4')
print(dt)
dt = np.dtype('<i4')
print(dt)
dt = np.dtype([('age',np.int8)])
print(dt)