import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.patches as patches

np.random.seed(10231)
x = np.random.normal([-1, -1], [.25, .25], size=(50, 2))
y = np.array([1, 1]).reshape(1, 2)

F = pd.DataFrame(np.concatenate([x, y]),  columns=['x', 'y'])
F['size'] = np.array([4]*51)
F['size'].iloc[50] = 16
F['distance'] = np.sqrt((F['x']-1)**2+(F['y']-1)**2)
j = sns.scatterplot(x='x', y='y', size='size', data=F, legend=None, hue='size', palette='tab20')
sns.set_style('darkgrid')

j.set_xlim([-2, 2])
j.set_ylim([-2, 2])
j.plot([1, -.5], [1, -.5], linewidth=2, linestyle='--', alpha=0.5, color='red')
j.plot([-.5, -1], [-.5, -1], linewidth=2, linestyle=':', alpha=0.5, color='red')
minrow = F['distance'].iloc[:50].idxmin()
(xmin,  ymin) = F[['x', 'y']].iloc[minrow, 0:2]
j.plot([1, xmin], [1, ymin], linewidth=2, linestyle='--', alpha=0.5,  color='blue')
j.set_aspect('equal')
j.add_patch(patches.Circle((-1, -1),  .75,  alpha=.05,  facecolor='red',  edgecolor='black',  linewidth=1,   linestyle='solid'))
j.get_figure().savefig('../png/cluster_distance.png')




