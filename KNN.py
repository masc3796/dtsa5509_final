import pickle
import sklearn
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pylab as plt
import random
from sklearn.model_selection import cross_val_score, GridSearchCV
import warnings

warnings.filterwarnings('ignore')

def show_image(Xdata):
    fig = plt.figure(figsize=(3,3))
    plt.imshow(Xdata.reshape(120, 128, 3), cmap='gray')
    plt.show()
    
with open("sunglasses_on.pickle", "rb") as f:
    X, y = pickle.load(f)
    
parameters = {
    "n_neighbors" : np.asarray([i for i in range(2, 7)]), 
    "weights" : ["uniform", "distance"], 
    
}

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.50)

clf = KNeighborsClassifier()
grid = GridSearchCV(clf, parameters, cv= 3)
grid.fit(X_train, y_train)

print("best params", grid.best_params_)

clf = grid.best_estimator_
y_pred = clf.predict(X_test)

print(accuracy_score(y_test, y_pred))

for i in range(10):
    r = random.randint(0, len(X_test)-1)

    actual = y_test[r]
    predicted = y_pred[r]

    print(f"Actual = {actual}, Predicted = {predicted}, success = {actual==predicted}")
    show_image(X_test[r])
    



