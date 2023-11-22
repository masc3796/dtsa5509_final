import pickle
import skimage
import numpy as np
import pandas as pd
import csv

df = pd.read_csv("data_index.csv")
df.info()

def serialize_and_pickle(y_label):
    X = []
    y = []

    for i in range(len(df)):
        fname = df["path"][i]
        
        d = skimage.io.imread(fname)

        #linearize the data to 1D array
        d = d.reshape(np.prod(d.shape))
        X.append(d)
        y.append(df[y_label][i])
        
    data = (np.asarray(X), np.asarray(y))
    with open(y_label+".pickle", "wb") as f:
        pickle.dump(data, f)
        
    
serialize_and_pickle("sunglasses_on")
serialize_and_pickle("direction_left")
serialize_and_pickle("direction_right")
serialize_and_pickle("direction_straight")
serialize_and_pickle("direction_up")
serialize_and_pickle("mood_angry")
serialize_and_pickle("mood_happy")
serialize_and_pickle("mood_neutral")
serialize_and_pickle("mood_sad")


