import pandas as pd 
import pickle
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# Read from input
x_df = pd.read_csv('x.csv')
y_df = pd.read_csv('y.csv')
z_df = pd.read_csv('z.csv')

# Organize and set up dataframe
df = pd.DataFrame({'x': x_df.columns, 'y': y_df.columns})

outlist = [ (i, j)
    for i in df['x']
    for j in df['y'] ]
newdf = pd.DataFrame(data=outlist, columns =['x', 'y'])


z_column_list = []
for col in z_df.columns:
    z_column_list.append(float(col))

temp_df = pd.DataFrame(data=z_column_list)

transposed_df = z_df.stack().values

final_z_list = []
for i in z_column_list:
    final_z_list.append(i)
for i in transposed_df:
    final_z_list.append(i)


newdf['z'] = final_z_list
df = newdf

# Obtain training and testing values
x_train, x_test, y_train, y_test = train_test_split(df.drop(['z'], axis=1), df['z'], test_size = 0.20, random_state=22)

# Scaling (optional)
# sc = StandardScaler()
# x_train = sc.fit_transform(x_train)
# x_test = sc.transform(x_test)

# Model setup and predict
model = MLPRegressor(solver='lbfgs', hidden_layer_sizes=(4,4,4), max_iter=500).fit(x_train, y_train)

# Save the model using pickle
filename = 'part1_finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

# Now use this generated model to predict z values :)
