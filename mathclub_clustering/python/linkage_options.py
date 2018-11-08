import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
np.random.seed(10231)




def animate_cluster(F, linkage, path):

    clusters = AgglomerativeClustering(n_clusters=2, linkage=linkage)
    j = clusters.fit_predict(F.values)

    A = np.zeros(F.shape[0])
    for i, x in enumerate(clusters.children_):
        for j in x:
            if j<F.shape[0]:
                A[j] = i

    F['level'] = A

    fig, j = plt.subplots(1)
    j.set_xlim([-2, 2])
    j.set_ylim([-2, 2])
    j.set_aspect('equal')
    sns.set_style('darkgrid')


    for i in range(0, int(A.max()), 5):
        G = F[F['level'] <= i]
        j = sns.scatterplot(x='x', y='y', data=G, legend=None, hue='group')
        j.get_figure().savefig('../png/'+path+'/'+path+'_'+str(i)+'.png')


        
x0 = np.random.multivariate_normal([.25, .25], cov=[[1, -.20],[-.20,.1]], size=50)
x1 = np.random.multivariate_normal([-.25, -.25], cov=[[1, -.25],[-.25,.1]], size=50)
F = pd.DataFrame(np.concatenate([x0, x1]),  columns=['x', 'y'])
F['group'] = np.array([0]*50+[1]*50)
j = sns.scatterplot(x='x', y='y',  data=F, legend=None, hue='group')
j.set_xlim([-2, 2])
j.set_ylim([-2, 2])
j.set_aspect('equal')
j = sns.scatterplot(x='x', y='y',  data=F, legend=None, hue='group')
j.get_figure().savefig('../png/base_data_for_linkage.png')
animate_cluster(F, 'single', 'single_stretch')
animate_cluster(F, 'ward', 'ward_stretch')



