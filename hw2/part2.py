import pandas as pd 
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
from pprint import pprint
from sklearn.mixture import GaussianMixture


# Read from input and put into dataframe
data = pd.read_csv('p2-data', header=None)
data.columns = ['a', 'b']
pprint(data)

# Cluster n_component estimation
# indentifies ideal number of clusters for data
n_components = np.arange(1, 21)
models = [GaussianMixture(n, covariance_type='full', random_state=0).fit(data)
          for n in n_components]

# Plot the calculated ideal cluster estimation
plt.plot(n_components, [m.bic(data) for m in models], label='BIC')
plt.plot(n_components, [m.aic(data) for m in models], label='AIC')
plt.legend(loc='best')
plt.xlabel('n_components');
plt.show()
plt.close()

# Set up and execute Gaussian model
gmm = GaussianMixture(n_components=5, covariance_type='full').fit(data)

# obtain mean (centers) of clusters
means = gmm.means_
pprint(means)

# obtain covariances of clusters
covariances = gmm.covariances_
pprint(covariances)

labels = gmm.predict(data)
plt.scatter(data['a'], data['b'], c=labels, s=40, cmap='viridis')
plt.show()





