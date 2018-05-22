# %load ec3.py
from math import factorial, gcd, log
import pickle
import numpy as np
import gmpy2

with open('primes10000.pickle','rb') as f:
    Primes10000=pickle.load(f)
                                                                                                                                                                                                             
def ecm(N,arange=100,krange=10000):
    for a in range(-arange,arange):
        x,y=0,1
        for B in Primes10000:
            k=B**(int(log(10000)/log(B)))
            sx,sy,t=x,y,k
            first=True
            while t>0:
                if t%2==1:
                    if first:
                        xm,ym=sx,sy
                        first=False
                    else:
                        # x1=xm,y1=ym, x2=sx,y2=sy,a=a,b=1,N=N
                        d,u,v=gmpy2.gcdext(sx-xm,N)
                        if d>1:
                            if d==N:
                                break
                            else:
                                return d
                        L=(u*(sy-ym)) % N
                        x_sum=(L*L-xm-sx) % N
                        ym=(L*(xm-x_sum)-ym) % N
                        xm=x_sum
                # sx=x,sy=y,a=a,b=1,N
                d,u,v=gmpy2.gcdext(2*sy,N)
                if d>1:
                    if d==N:
                        break
                    else:
                        return d
                L=(u*(3*sx*sx+a)) % N
                x2=(L*L-2*sx) % N
                sy=(L*(sx-x2)-sy) %N
                sx=x2
                t=t//2
            x,y=xm,ym
    print('Failed')



N=2**(128)+1
print('answer is', ecm(N,arange=100,krange=10000),flush=True)




