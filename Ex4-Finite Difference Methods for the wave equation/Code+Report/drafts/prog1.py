from math import ceil
import numpy as np
import matplotlib.pyplot as plt

def g0(x):
	absx = np.abs(x)
	return np.where(absx > 1, 0, 1-absx)

def g1(x):
	return np.zeros(x.size)

#t = 0.1
t = eval(input("Choose a t: \nt="))

alpha = 1;  lam=0.5 ; T = t; #T = 0.30;  lam = 0.5
J = 199;  h = 1.0/(J+1);  x = np.linspace(-3, 3, J+2)
k = lam * h / alpha;  N = ceil(T/k)

a = (lam**2)*np.ones(J-1);  b = (2*(1-lam**2))*np.ones(J);
A = np.diag(a, -1) + np.diag(b, 0) + np.diag(a, 1)

U = g0(x[1:J+1])
V = 0.5*A.dot(U) + alpha**2 * k * g1(x[1:J+1])

for n in range(1,N):
	tmp = A.dot(V) - U
	for j in range(J): U[j] = V[j]; V[j] = tmp[j]

#plt.plot(x, u0(x-t), 'k-')#, linewidth=1.5)
plt.plot(x[1:J+1], V) #, 'b-o')
#plt.ylim(-0.1, 1.1)
plt.title('$\lambda = %g \quad h = %g \quad t = %g$' % (lam, h, t))
#plt.savefig('upwind.png')
plt.show()

