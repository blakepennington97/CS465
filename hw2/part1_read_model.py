import pandas as pd 
import seaborn as sns
import csv
import matplotlib.pyplot as plt
import pickle
from sklearn import metrics

# Read from input
x_df = pd.read_csv('x_test.csv')
y_df = pd.read_csv('y_test.csv')

# Organize and set up dataframe
df = pd.DataFrame({'x': x_df.columns, 'y': y_df.columns})

outlist = [ (i, j)
    for i in df['x']
    for j in df['y'] ]
newdf = pd.DataFrame(data=outlist, columns =['x', 'y'])

# Load model from disk
loaded_model = pickle.load(open('part1_finalized_model.sav', 'rb'))

# Predict the z values
predicted_z = loaded_model.predict(newdf)

# Format predicted z values to write to CSV
results = [[0 for i in range(30)] for j in range(30)]
for i in range(900):
    results[int(i / 30)][i % 30] = predicted_z[i]


# Write predicted z results to z-predicted.csv
with open('z-predicted.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in results:
        writer.writerow(i)

# Grab given z results to compare vs the predicted
z_df = pd.read_csv('z.csv')
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

# Give estimation on accuracy of the model
print("Estimated model accuracy: ", metrics.r2_score(final_z_list, predicted_z))

# Plot to compare given z vs predicted z results
plt.style.use('ggplot')
plt.figure(figsize=(10,10))
sns.regplot(x=final_z_list, y=predicted_z, fit_reg=True, scatter_kws={"s": 100}).set(title='Given z vs predicted z results', xlabel='Given z values', ylabel='Predicted z results')
plt.show()