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
            k=10000
            while k>0:
                k=k//B
                sx,sy,t=x,y,B
                first=True
                while True:
                    if t%2==1:
                        if first:
                            xm,ym=sx,sy
                            first=False
                        else:
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
                    t=t//2
                    if t==0:
                        break
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
                x,y=xm,ym
    print('Failed')


# First factored in 1980 by Brent and Pollard using rho method
# Factorization of the Eighth Fermat Number
# Richard Brent, John Pollard
# Mathematics of Computation, Volume 36, Number 154, April 1981
#V=1238926361552897
#N=2**(256)+1
#print('Factor of F8', ecm(N,arange=100,krange=10000),flush=True)

# These smaller factors were found in 1988 by Brent

N=2**(2**11)+1
d1=ecm(N,arange=100,krange=10000)
print(d1)
d2=ecm(N//d1)
print(d2)
M=N//(d1*d2)
d3=ecm(M)
print(d3)
d4=ecm(M//d3)
print('Factors of F11',d1,d2,d3,d4,flush=True)




