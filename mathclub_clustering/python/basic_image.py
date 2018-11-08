import sklearn
import pandas as pd
import numpy as np
import seaborn as sns


def trunc(x):

    if x < -3:
        return -3

    if x > 3:
        return 3
    return x


vtrunc = np.vectorize(trunc)
M = pd.read_csv('../data/labelled_data.csv', index_col=0)
genes = M.columns[2:]

sns.set_style('white')
Xs = sklearn.preprocessing.StandardScaler(copy=True).fit_transform(M[genes].values)
j = sns.heatmap(vtrunc(Xs))
j.set_title('Raw Data: 800 rows and ~20K columns')
j.get_figure().savefig('../png/basic_image.png')
