from math import ceil
import numpy as np
import matplotlib.pyplot as plt


global L, targetN, targetT
global pl_num #tha to xreiastw sto plotting,
# antistoixei se poio subplot vriskomai i-osto

def g0(x):
	return np.exp(-5*(x-2)**2)

def g1(x):
	return np.zeros(x.size)

L=4; alpha = 1;  lam=0.8 ; T = 1;
h = 0.01; J = ceil(4/h -1); x = np.linspace(0, L, J+2)
k = lam * h / alpha;  N = ceil(T/k)
#print(J)
targetT = [0.25, 0.5, 0.75, 1]
targetN = [ceil(tn/k) for tn in targetT]
pl_num = 1

a = (lam**2)*np.ones(J);  b = (2*(1-lam**2))*np.ones(J+1);
A = np.diag(a, -1) + np.diag(b, 0) + np.diag(a, 1)
A[0][J] = lam**2; A[J][0]=lam**2


U = g0(x[0:J+1])
V = 0.5*A.dot(U) + alpha**2 * k * g1(x[0:J+1])


#plot_subplot_for_n(0)

pl_num=1
for n in range(1,N):
    tmp = A.dot(V) - U
    for j in range(J): U[j] = V[j]; V[j] = tmp[j]

    if n+1 in targetN: 
        sub = int("41"+str(pl_num))
        plt.subplot(sub)
        plt.plot(x[0:J+1], V)
        plt.title('t = %g' %targetT[targetN.index(n+1)])

#        plt.axis([0, L, -0.1, 0.8]) 
        pl_num+=1

plt.tight_layout()
plt.savefig('wave.png')
plt.show()
