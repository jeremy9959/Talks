import numpy as np
import pandas as pd
import seaborn as sns

np.random.seed(12)

x0 = np.random.normal([-1,-1],[.25, .25],size=(50,2))
x1 = np.random.normal([1,.5],[.25, .25],size=(50,2))
x2 = np.random.normal([-1,.5],[.25,.25],size=(50,2))
z = [0]*50 + [1]*50+  [2]*50
F=pd.DataFrame(np.concatenate([x0,x1,x2]),columns=['x','y'])
F['color']=z
sns.set_style('darkgrid')
j = sns.scatterplot(x='x',y='y',data=F)
j.get_figure().savefig('../png/basic.png')

k = sns.scatterplot(x='x',y='y',legend=None,hue='color', data=F,palette='tab10')
k.get_figure().savefig('../png/basic_1.png')

