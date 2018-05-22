import numpy as np
import pickle



P=np.zeros(10000)
P[0]=1
P[1]=1
for i in range(2,10000):
    if P[i]==0:
        j=2
        while i*j<1000:
            P[i*j]=1
            j=j+1

Primes10000=[i for i,x in enumerate(P) if x==0]
with open('primes10000.pickle','wb') as f:
    pickle.dump(Primes10000,f)
