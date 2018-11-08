import matplotlib.pyplot as plt

x0=np.array([[-1,0],[0,0],[1,0]])
x1=np.array([[3,0],[4,0],[5,0]])
x2=np.array([[-1,-3],[0,-3],[1,-3]])

fig,ax=plt.subplots(1)
ax.grid()
ax.set_xlim([-8,8])
ax.set_ylim([-8,8])

plt.scatter(x0[:,0],x0[:,1])
plt.scatter(x1[:,0],x1[:,1])
plt.scatter(x2[:,0],x2[:,1])
plt.plot([0,4],[0,0],color='red')
plt.plot([0,4],[-3,0],color='red')
plt.plot([0,0],[0,-3],color='red')
fig.savefig('centroid.png')
