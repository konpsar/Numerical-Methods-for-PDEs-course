from math import ceil
import numpy as np
import matplotlib.pyplot as plt

#Ut + aUx =0 gia -2<=x<=3 kai t>=0
#me a.s. U0(x) = 1-|x| gia |x|<=1, 0 diaforetika
#kai sunoriakh U(-2, t)=0. psaxnw sto t=1.6
#akrivhs lush U(x, 1.6) = U0(x-1.6) gia -2<=x-1.6, 0 diaforetika


def u0(x):
	ax = np.abs(x)
	return np.where(ax > 1, 0, 1 - ax)

alpha = 1
a = -2;  b = 3;  J = 49;  h = (b - a) / (J+1)
x = np.linspace(-2, 3, J+2)
lam = 0.8;  k = lam * h;  t = 1.6;  N = ceil(t/k)

U = u0(x);  V = np.zeros(J+2)

for n in range(N):

	for j in range(J+1): 
		#Lax-Friedrichs
		V[j] = 1/2*( U[j+1] + U[j-1] - lam * alpha * ( U[j+1] - U[j-1] ) )
		#Downwind
		#V[j] = U[j] - lam * alpha * ( U[j+1] - U[j] )
		#Upwind
		#V[j] = U[j] - lam * alpha * ( U[j] - U[j-1] )
	for j in range(J+1): 
		U[j] = V[j]

plt.plot(x, u0(x-t), 'k-')#, linewidth=1.5)
plt.plot(x, U, 'b-o')
plt.ylim(-0.1, 1.1)
plt.title('$\lambda = %g \quad h = %g \quad t = %g$' % (lam, h, t))
#plt.savefig('upwind.png')
plt.show()
