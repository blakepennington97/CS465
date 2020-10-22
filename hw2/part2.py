import pandas as pd 
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
from pprint import pprint
from sklearn.mixture import GaussianMixture


# Read from input and put into dataframe
data = pd.read_csv('p2-data', header=None)
data.columns = ['a', 'b']

# Cluster n_component estimation
# indentifies ideal number of clusters for data
n_components = np.arange(1, 21)
models = [GaussianMixture(n, covariance_type='full', random_state=0).fit(data)
          for n in n_components]

# Plot the calculated ideal cluster estimation
# uncomment these lines below to view optimal number of clusters
# plt.plot(n_components, [m.bic(data) for m in models], label='BIC')
# plt.plot(n_components, [m.aic(data) for m in models], label='AIC')
# plt.legend(loc='best')
# plt.xlabel('n_components');
# plt.show()

# Set up and execute Gaussian model
gmm = GaussianMixture(n_components=5, covariance_type='full').fit(data)

# Obtain mean (centers) of clusters
means = gmm.means_
print("Mean of clusters: \n")
j = 1
for i in means:
    print("Cluster ", j)
    print(i)
    j += 1
print("\n\n\n")

# Obtain covariances of clusters
covariances = gmm.covariances_
print("Covariances of clusters: \n")
j = 1
for i in covariances:
    print("Cluster ", j)
    print(i)
    j += 1

labels = gmm.predict(data)
plt.scatter(data['a'], data['b'], c=labels, s=40, cmap='viridis')
plt.show()





