# %%
import numpy as np
from numpy.random import default_rng
gen = default_rng()
cov = np.array([[4, -1],[-1,2]])
data = gen.multivariate_normal([0,0],cov,size=500)
datazero= data - data.mean(axis=0)

# %%
from bokeh.plotting import figure, output_notebook, show
from bokeh.io import export_png
from bokeh.models import Range1d
output_notebook()
# %%
f=figure(title="Sample Data",aspect_scale=1.0)
f.scatter(x=datazero[:,0],y=datazero[:,1],alpha=.5)
f.x_range=Range1d(-6,6)
f.y_range=Range1d(-6,6)
show(f)
export_png(f,filename="sample_data.png")
# %%
D = 1/500 * (datazero.transpose() @ datazero)
# %%
D
# %%
L, P = np.linalg.eigh(D)
# %%
print(P,L)
# %%
P @ np.diag(L) @ P.transpose()
# %%
t=np.linspace(-10,10,21)
x1=-.41*t
y1 = -.91 *t
x2 = -.91*t
y2 = .41*t
f.title="Sample Data with Eigenvector Directions"
f.line(x=x1,y=y1,color='red')
f.scatter(x=x1,y=y1,color='red',size=4 )
f.line(x=x2,y=y2,color='red')
f.scatter(x=x2,y=y2,color='red',size=4)
show(f)
export_png(f,filename="pcplot.png")
# %%
t
# %%
data0 = default_rng().multivariate_normal([-2,-3,2,5],cov=np.diag([1,2,2,1]),size=20)
data1 = default_rng().multivariate_normal([2,-1,-1,2],cov=np.diag([1,1,1,1]),size=20)
# %%
joined = np.concatenate([data0,data1],axis=0)
# %%
joined = joined-joined.mean(axis=0)
# %%
f1=figure(title='Scatterplot of selected features')
f1.scatter(x=joined[:,3],y=joined[:,1])
show(f1)
export_png(f1,filename="selected.png")
# %%
from seaborn import pairplot
import pandas as pd
df = pd.DataFrame(joined)
pairplot(df)
# %%
df.shape
# %%
df
# %%
D=(1/40)*(joined.transpose())@(joined)
L, P = np.linalg.eigh(D)

# %%
print(L)
# %%
print(P)
# %%
S = joined @ P[:,-2:]
# %%
S
# %%
f3 = figure(title="Most important directions")
f3.scatter(x=S[:,0],y=S[:,1])
show(f3)
export_png(f3,filename='pc_scatter.png')
# %%
