from math import ceil
import numpy as np
import matplotlib.pyplot as plt


global L, targetN, targetT
global pl_num #tha to xreiastw sto plotting,
# antistoixei se poio subplot vriskomai i-osto
L=4; alpha = 1;  lam=0.8 ; T = 1;
h = 0.01; J = ceil(1/h -1); x = np.linspace(0, L, J+2)
k = lam * h / alpha;  N = ceil(T/k)

targetT = [0, 0.25, 0.5, 0.75]
targetN = [ceil(tn/k) for tn in targetT]
pl_num = 1

def g0(x):
	return np.exp(-5*(x-2)**2)

def g1(x):
	return np.zeros(x.size)

def plot_subplot_for_n(n):
        global pl_num, L, axes_limit, targetT, targetN
        sub = int("41"+str(pl_num))
        plt.subplot(sub)
        plt.plot(x[1:J+1], V)
        plt.title('t = %g' %targetT[targetN.index(n)])
        plt.axis([0, L, -1, 1])
        pl_num+=1


a = (lam**2)*np.ones(J-1);  b = (2*(1-lam**2))*np.ones(J);
A = np.diag(a, -1) + np.diag(b, 0) + np.diag(a, 1)

U = g0(x[1:J+1])
V = 0.5*A.dot(U) + alpha**2 * k * g1(x[1:J+1])


plot_subplot_for_n(0)

for n in range(1,N):
    tmp = A.dot(V) - U
    for j in range(J): U[j] = V[j]; V[j] = tmp[j]

    if n in targetN: plot_subplot_for_n(n)

plt.tight_layout()
plt.savefig('wave.png')
plt.show()
