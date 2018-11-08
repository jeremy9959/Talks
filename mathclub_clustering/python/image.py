import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing
import pandas as pd
import numpy as np

def trunc(x):
    if x<-3:
        return -3
    if x>3:
        return 3
    return x


vtrunc = np.vectorize(trunc)
M = pd.read_csv('../data/labelled_data.csv',index_col=0)
genes = M.columns[2:]

fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,10))

Xs=sklearn.preprocessing.StandardScaler(copy=True).fit_transform(M[genes].values)
axes[0].imshow(vtrunc(Xs),aspect='auto',cmap='inferno')
axes[0].set_title('Raw Data')

Msorted = M.sort_values('Type')
Xs1=sklearn.preprocessing.StandardScaler(copy=True).fit_transform(Msorted[genes].values)
axes[1].imshow(vtrunc(Xs1),aspect='auto',cmap='inferno')
axes[1].set_title('Sorted by Type')
fig.savefig('../png/image.png')
