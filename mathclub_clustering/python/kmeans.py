import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

M = pd.read_csv('../data/labelled_data.csv',index_col=0)
genes = M.columns[2:]
N=pd.DataFrame(PCA(n_components=2).fit_transform(M[genes].values),columns=['x','y'],index=M.index)

km = KMeans(n_clusters=5).fit(N.values)
predicted_cluster=km.predict(N.values)
N['Predicted']=[int(x) for x in predicted_cluster]

KM = pd.DataFrame(km.cluster_centers_, columns=['x','y'])
sns_plot=sns.scatterplot(x='x',y='y', hue='Predicted',legend='full',data=N,alpha=0.5)
sns.scatterplot(x='x', y='y', data=KM, ax=sns_plot,color='green',s=64)
sns_plot.set_title('KMeans Centers and Clusters with N=5')
sns_plot.get_figure().savefig('../png/kmeans.png')
