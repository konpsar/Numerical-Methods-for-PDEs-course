import numpy as np
import matplotlib.pyplot as plt

def u0(x): return x*(1-x)
J = 20; dx = 1.0 /  J;  x = np.linspace(0, 1, J+1)
N = 450 ; T = 0.5; dt = T / N 
mu = dt / dx**2
U = u0(x); U[0] = 0; U[J] = 0
V = np.zeros(J+1)
Un = np.max(abs(U))
print(mu)
for n in range(N):
	for j in range(1,J):
		V[j] = U[j] + mu * ( U[j+1] - 2*U[j] + U[j-1] )
	for j in range(1,J):
		U[j] = V[j]
print (Un)

plt.plot(x, U, 'b-')
plt.show()
