import pandas as pd 
import seaborn as sb
import csv
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from pprint import pprint



x_df = pd.read_csv('x.csv')
y_df = pd.read_csv('y.csv')
z_df = pd.read_csv('z.csv')

df = pd.DataFrame({'x': x_df.columns, 'y': y_df.columns})

outlist = [ (i, j)
    for i in df['x']
    for j in df['y'] ]
newdf = pd.DataFrame(data=outlist, columns =['x', 'y'])


z_column_list = []
for col in z_df.columns:
    z_column_list.append(float(col))

temp_df = (pd.DataFrame(data=z_column_list))

transposed_df = z_df.transpose().stack().values

final_z_list = []
for i in z_column_list:
    final_z_list.append(i)
for i in transposed_df:
    final_z_list.append(i)


newdf['z'] = final_z_list

pprint(newdf)

df = newdf

X, y = make_regression(n_samples=200, random_state=1)

# pprint(X)
# pprint([df['x'], df['y']])


x_train, x_test, y_train, y_test = train_test_split(df.drop('z', axis=1), df['z'], test_size = 0.2, random_state=1)


model = MLPRegressor(random_state=1, max_iter=500).fit(x_train, y_train)
result1 = model.predict(x_test[:2])
result2 = model.score(x_test, y_test)

pprint(result1)
pprint(result2)

#regr = MLPRegressor(random_state=1, max_iter=500).fit(x_train, y_train)

#print(regr.predict(x_test[:2]))
#print(regr.score(x_test, y_test))



# print(x_data.head)
# print(y_data.head)