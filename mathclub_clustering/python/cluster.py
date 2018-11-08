import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA
# Data from https://archive.ics.uci.edu/ml/datasets/gene+expression+cancer+RNA-Seq
J=pd.read_csv('../data/data.csv')
J.index=J['Unnamed: 0']
J.index.name='sample'
J=J[J.columns[1:]]
N=pd.DataFrame(PCA(n_components=2).fit_transform(J.values),columns=['x','y'],index=J.index)
N.index.name='sample'

K=pd.read_csv('labels.csv')
cancer_names={'BRCA':'Breast','LUAD':'Lung','KIRC':'Kidney','COAD':'Colon', 'PRAD':'Prostate'}
K.index=K['Unnamed: 0']
K=K[['Class']]
K.index.name='sample'
K['Type']=K['Class'].map(cancer_names)

K=K.join(N)

sns.set_style('darkgrid')
sns_plot=sns.scatterplot(x='x',y='y',hue='Type',data=K)
sns_plot.set_title('Principal Components of RNA-seq Profiles\n for different cancer types')
sns_plot.get_figure().savefig('../png/cluster.png')


K.to_csv('pca_data.csv')

