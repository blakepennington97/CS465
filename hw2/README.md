# CS465 HW1

This is a repository that uses both supervised and unsupervised algorithms to predict and analyze data.

## Part 1

There exists a nonlinear relationship between input attributes x and y and output target z. The training set consists of 30 noisy samples.

Using a parametric supervised training method, which in this case is a multi-layer perceptron regressor, the model is able to accurately predict
the outcome of z values given the attributes x and y.

![Image of Multi-layer Perceptron](https://miro.medium.com/max/3446/1*-IPQlOd46dlsutIbUq1Zcw.png)

**To execute Part 1, there are **two** steps:**
    1. First, run 'part1_create_model.py' with your desired x, y, and z values in the x.csv, y.csv, and z.csv files. This will generate and save a model that can be used during the second step.

    2. Second, run 'part1_read_model.py' with your desired x and y test values in the x_test.csv and y_test.csv files. This will result in agenerated table of  predicted z values within z-predicted.csv

**About Part 1**:
    The model of a multi-layer perceptron regressor was chosen over others is because TODO. The number (4,4,4) of hidden layer nodes was chosen because it seemed best suited to the sample size of the given data for the assignment. Max iterations during the training was raised from 200 to 500 for better approximations. I chose this model complexity with empirical loss over the training set because TODO.


## Part 2

This program uses an unsupervised learning method, which in this case is the Gaussian Mixture Model, to identify clusters of similar data. The program also outputs the mean (center) of clusters and covariance of individual clusters.

For reference, the file p2-data was used as the dataset for this program.

About Part 2:
    Out of all the clustering methods available, the Guassian Mixture Model was chosen for this assignment due to how it fit to the data in the most ideal way. K-means works with more circular blobs, while GMM works well with abitrarily shaped data blobs. The data in p2-data dataset is more oriented towards the latter. K-means was chosen first to test clustering on the dataset. Although it is extremely efficient, it's simplistic nature limits how well the clusters can be fitted. Here is an example image of what was experienced.
    ![Image of covariance parameters]https://qph.fs.quoracdn.net/main-qimg-17cc6dcd28056b547ba49486749696df

    In order to identify the ideal number of clusters, TODO was implemented.
    The reasoning of using the parameter of using 'full' TODO
    ![Image of covariance parameters](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_covariances_0011.png)





Requirements:
    Python 3.6
    sklearn
    pandas
    numpy
    pickle
    seaborn
    matplotlib
    
    
Sources used:
    https://github.com/aimacode/aima-python/blob/master/probability4e.ipynb
    
