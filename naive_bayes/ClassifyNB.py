def classify(features_train, labels_train):
### import the sklearn module for GaussianNB
### create classifier
### fit the classifier on the training features and labels
### return the fit classifier


### your code goes here!

    import numpy as np
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    Y = np.array([1, 1, 1, 2, 2, 2])
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(X, Y)
    GaussianNB(priors=None)