import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# a very crude hierarchical clustering demo

sns.set_style('whitegrid')
N=30
c=[(1,1),(2,0),(-2,-1)]

def mk_pts(N,c):
    X=np.random.normal(c[0],.5,size=(N,2))
    for x in c[1:]:
        Y=np.random.normal(x,.5,size=(N,2))
        X=np.concatenate([X,Y])
    return(X)


def dist_matrix(A):
    D=np.zeros([A.shape[0],A.shape[0]])
    for i in range(A.shape[0]):
        for j in range(i+1,A.shape[0]):
            D[i,j]=np.sum(np.power(A[i,:]-A[j,:],2))
    return D


def closest(B):
    i,j=np.where(B==np.min(B[np.nonzero(B)]))
    return i[0],j[0]


def update(A,I,T):
    D=dist_matrix(A)
    i,j = closest(D)
    z=((A[i,:]+A[j,:])/2).reshape(1,2)
    A=np.delete(A,[i,j],axis=0)
    A=np.concatenate([A,z])
    new_node=np.max(I)+1
    T[I[i]]=new_node
    T[I[j]]=new_node
    I=[x for x in I if (x!=I[i] and x!=I[j])]
    I.append(new_node)
    return A,I,T

    
def find_clust(k,A):
    M=A.shape[0]
    I=[i for i in range(M)]
    T={}
    while A.shape[0]>k:
        A,I,T=update(A,I,T)

    C={}
    for i in range(M):
        j=i
        while j in T:
            j=T[j]
        if j in C:
            C[j].append(i)
        else:
            C[j]=[i]
        
    return C
        
        
    
fig,axes=plt.subplots(3,1,figsize=(10,10),sharex=True)

A=mk_pts(N,c)
F=pd.DataFrame(A,columns=['x','y'])
sns.scatterplot(x='x',y='y',data=F,palette='tab20',ax=axes[0])

H=find_clust(3,A)

y=np.zeros(A.shape[0])
s={}
for i, t in enumerate(H.keys()):
    s[t]=i
for x, t in H.items():
    y[t]=s[x]
F['predicted']=y
sns.scatterplot(x='x',y='y',hue='predicted',legend=None,data=F,palette='tab20',ax=axes[1])
fig.suptitle('Hierarchical Clustering')
axes[0].set_title('Original Data')
axes[1].set_title('With 3 Clusters')

H1=find_clust(8,A)
y=np.zeros(A.shape[0])
s={}
for i, t in enumerate(H1.keys()):
    s[t]=i
for x, t in H1.items():
    y[t]=s[x]
F['predicted']=y
sns.scatterplot(x='x',y='y',hue='predicted',legend=None,data=F,palette='tab20',ax=axes[2])
axes[2].set_title('With 8 Clusters')



fig.savefig('Hierarchical.png')

