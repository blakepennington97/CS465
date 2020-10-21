import pandas as pd 
import numpy as np
import seaborn as sns; sns.set()
import csv
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from pprint import pprint
from sklearn import datasets
from sklearn.mixture import GaussianMixture


# read from input and put into dataframe
data = pd.read_csv('p2-data', header=None)
data.columns = ['a', 'b']
pprint(data)

# setup gmm
gmm = GaussianMixture(n_components=5).fit(data)
labels = gmm.predict(data)
plt.scatter(data['a'], data['b'], s=40, cmap='viridis')
plt.show()
plt.scatter(data['a'], data['b'], c=labels, s=40, cmap='viridis')
plt.show()



