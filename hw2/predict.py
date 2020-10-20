import pandas as pd 
import seaborn as sns
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


# read from input
x_df = pd.read_csv('x.csv')
y_df = pd.read_csv('y.csv')
z_df = pd.read_csv('z.csv')

# organize and set up dataframe
df = pd.DataFrame({'x': x_df.columns, 'y': y_df.columns})

outlist = [ (i, j)
    for i in df['x']
    for j in df['y'] ]
newdf = pd.DataFrame(data=outlist, columns =['x', 'y'])


z_column_list = []
for col in z_df.columns:
    z_column_list.append(float(col))

temp_df = pd.DataFrame(data=z_column_list)
# pprint(temp_df)

transposed_df = z_df.stack().values
pprint(transposed_df)

final_z_list = []
for i in z_column_list:
    final_z_list.append(i)
for i in transposed_df:
    final_z_list.append(i)

pprint(final_z_list)


newdf['z'] = final_z_list
df = newdf
pprint(df)
dataset = datasets.load_wine()
# pprint(dataset.data)
# pprint(dataset.target)
# print()
# pprint(df.drop('z', axis=1).values)
# pprint(df['z'].values)

# obtain training and testing values
x_train, x_test, y_train, y_test = train_test_split(df.drop(['z'], axis=1), df['z'], test_size = 0.20, random_state=22)

# scaling
# sc = StandardScaler()
# x_train = sc.fit_transform(x_train)
# x_test = sc.transform(x_test)

# model setup and predict
model = MLPRegressor(hidden_layer_sizes=(4,4,4), max_iter=500).fit(x_train, y_train)

expected_y = y_test
pprint(expected_y)

predicted_y = model.predict(x_test)
result2 = model.score(x_test, y_test)

pprint(predicted_y)
pprint(result2)

with open('z-predicted.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(predicted_y)



# plotting
plt.style.use('ggplot')
plt.figure(figsize=(10,10))
sns.regplot(x=expected_y, y=predicted_y, fit_reg=True, scatter_kws={"s": 100})
#plt.show()


