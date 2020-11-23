# CS465 HW2

This is a repository that uses both supervised and unsupervised algorithms to predict and analyze data.

## Part 1

There exists a nonlinear relationship between input attributes x and y and output target z. The training set consists of 30 noisy samples.

Using a parametric supervised training method, which in this case is a multi-layer perceptron regressor, the model is able to accurately predict
the outcome of z values given the attributes x and y.

![Image of Multi-layer Perceptron](https://miro.medium.com/max/3446/1*-IPQlOd46dlsutIbUq1Zcw.png)

**To execute Part 1, there are **two** steps:**
    
- First, run 'part1_create_model.py' with your desired x, y, and z values in the x.csv, y.csv, and z.csv files. This will generate and save a model that can be used during the second step.
- Usage `python3 part1_create_model.py`
- Second, run 'part1_read_model.py' with your desired x and y test values in the x_test.csv and y_test.csv files. This will result in agenerated table of  predicted z values within z-predicted.csv
- Usage `python3 part1_read_model.py`

**About Part 1**:
    
The model of a multi-layer perceptron regressor was chosen over others because it suits the exact use case Part 1 was designed for: predicting a real-valued value given a set of labeled inputs. The number (4,4,4) of hidden layer nodes was chosen because it seemed best suited to the sample size of the given data for the assignment. Max iterations during the training was raised from 200 to 500 for better approximations. I chose this model complexity with empirical loss over the training set because higher accuracy scores were achieved in testing when compared to other options.


## Part 2

This program uses an unsupervised learning method, which in this case is the Gaussian Mixture Model, to identify clusters of similar data. The program also outputs the mean (center) of clusters and covariance of individual clusters. At the end of execution, the program will show a comparison between the expected z values and predicted z values through a plot.

For reference, the file p2-data was used as the dataset for this program.

**To execute Part 2**
- Run part2.py with the desired data contained within p2-data
- Usage `python3 part2.py`


**About Part 2:**
    
Out of all the clustering methods available, the Guassian Mixture Model was chosen for this assignment due to how it fit to the data in the most ideal way. K-means works with more circular blobs, while GMM works well with abitrarily shaped data blobs. The data in p2-data dataset is more oriented towards the latter. K-means was chosen first to test clustering on the dataset. Although it is extremely efficient, it's simplistic nature limits how well the clusters can be fitted. Here is an example image of what was experienced.

![Image of covariance parameters](https://qph.fs.quoracdn.net/main-qimg-17cc6dcd28056b547ba49486749696df)

In order to identify the ideal number of clusters, the data was fitted against a range of cluster sizes to achieve the best result. These results were then graphed as shown below. Notice the parallel dip. That represents the ideal number of clusters for this dataset.

![Image of covariance parameters](https://imgur.com/YSGD3qX)

The reasoning of using the covariance parameter = 'full' was through trial and error testing, and understanding/theory of how this particular parameter worked. A spherical value would lean more towards a k-means-like result during testing. Empircal testing was used while exploring the covariance parameter. An average covariance value was calculated and compared against other parameters. In the end, full covariance won out as the ideal choice. An example image is shown below.

![Image of covariance parameters](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_covariances_0011.png)





**Requirements:**
    Python 3.6
    sklearn
    pandas
    numpy
    pickle
    seaborn
    matplotlib
    
    
**Sources used:**
    https://jakevdp.github.io/PythonDataScienceHandbook/05.12-gaussian-mixtures.html
    https://seaborn.pydata.org/generated/seaborn.regplot.html
    https://www.youtube.com/watch?v=0Lt9w-BxKFQ&feature=youtu.be
    https://www.dezyre.com/recipes/use-mlp-classifier-and-regressor-in-python
    https://scikit-learn.org/stable/modules/mixture.html
    https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html

