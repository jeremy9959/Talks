# %load ec3.py
from math import factorial, gcd, log
import numpy as np
P=np.zeros(1000)
P[0]=1
P[1]=1
for i in range(2,100):
    if P[i]==0:
        j=2
        while i*j<100:
            P[i*j]=1
            j=j+1
Primes1000=[i for i,x in enumerate(P) if x==0 ]  


def mexp(a,x,N):
    m,s=1,a
    while x>0:
        if x % 2 ==1:
            m=((m*s) % N)
        s=((s*s) % N)
        x=x//2
    return m

def euclid(u,v):
    if v==0:
        raise ArithmeticError('Division by Zero')
    x0,x1=u,v
    a0,a1=1,0
    b0,b1=0,1
    while x1!=0:
        q=x0//x1
        x2=x0-q*x1
        a2=a0-q*a1
        b2=b0-q*b1
        x0,a0,b0=x1,a1,b1
        x1,a1,b1=x2,a2,b2
    if x0<0:
        return -x0,-a0,-b0
    else:
        return x0,a0,b0

def mod_inv(u,N):
    d,a,b=euclid(u,N)
    if d==1:
        return a
    else:
        raise ArithmeticError('Common factor is '+str(d))

def two_p(x,y,a,b,N):
    Lu=(3*x**2+a) % N
   # print(Lu)
    Lb=mod_inv(2*y,N)
  #  print(Lb)
    L=Lu*Lb % N
    x_two=(L*L-2*x) % N
    y_two=(L*(x-x_two)-y) %N
    return x_two,y_two

def sum_p(x1,y1,x2,y2,a,b,N):
    Lu=(y2-y1) % N
    Lb=mod_inv(x2-x1,N)
    L=(Lu*Lb) % N
    x_sum=(L*L-x1-x2) %N
    y_sum=(L*(x1-x_sum)-y1) %N
    return x_sum,y_sum
    
def exp_p(x,y,a,b,m,N):
    sx,sy=x,y
    first=True
    while m>0:
        if m%2==1:
            if first:
                xm,ym=sx,sy
                first=False
            else:
                xm,ym=sum_p(xm,ym,sx,sy,a,b,N)
        sx,sy=two_p(sx,sy,a,b,N)
        m=m//2
    return xm,ym

#def mexp(a,x,N):
 #   m,s=1,a
 #   while x>0:
 #       if x % 2 ==1:
 #           m=((m*s) % N)
 #       s=((s*s) % N)
 #       x=x//2
 #   return m

def ecm_trial(N,arange=50,krange=30):
    for a in range(-arange,arange):
        xm,ym=0,1
        print(a) 
        for k in range(2,krange):
            try:
                xm,ym=exp_p(xm,ym,a,1,k,N)
            except ArithmeticError:
                print('try the following: a=',a,' and k=',k)
                break

                        
                    
#N=149185656432189838133
#ecm_trial(N,arange=20,krange=10000)
N=2**128+1
#ecm_trial(N,arange=100,krange=10000)
xm,ym=exp_p(0,1,-91,1,factorial(7883),N)
                                                                                                                                    
                                            


