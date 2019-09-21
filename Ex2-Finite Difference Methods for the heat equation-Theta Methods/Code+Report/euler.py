import numpy as np

def u0(x): return np.exp(x)*np.sin(2*np.pi*x)

J = 16; dx = 1/J;  x = np.linspace(0, 1, J+1)
N = 512 ; T = 0.5  ; dt = T / N 
mi = dt / dx**2; k = 0.2

#print(T, dt, mi, k)

U = u0(x); U[0] = 0; U[J] = 0
V = np.zeros(J+1)
Un = np.max(abs(U))

#print(U, Un)
for n in range(int(0.25*512)):
	for j in range(1,J):
		V[j] = U[j] + k* mi * ( U[j+1] - 2*U[j] + U[j-1] )
	for j in range(1,J):
		U[j] = V[j]
print(U[8])
print(x[8])

#print(0.1/dt)
#print(128*dt)
