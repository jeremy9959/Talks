import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import numpy as np

def trunc(x):
    if x<-3:
        return -3
    if x>3:
        return 3
    return x


vtrunc = np.vectorize(trunc)


M = pd.read_csv('../data/labelled_data.csv', index_col=0)
genes = M.columns[2:]
Xs = sklearn.preprocessing.StandardScaler(copy=True).fit_transform(M[genes].values)
clustering = AgglomerativeClustering(n_clusters=5).fit(Xs)

fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)

D = pd.DataFrame(Xs, columns=genes)
D['class'] = clustering.labels_
Dsorted = D.sort_values('class')
axes[1].imshow(np.transpose(vtrunc(Dsorted[genes].values)), aspect='auto', cmap='inferno')
axes[0].imshow(np.transpose(vtrunc(D[genes].values)), aspect='auto', cmap='inferno')
axes[0].set_title('Original Data')
axes[1].set_title('Data grouped into five clusters')
fig.suptitle('Clustering reveals hidden structure')
fig.savefig('../png/reveal.png')

