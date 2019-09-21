import numpy as np

# Initial conditon

def u0(x): return (x*(1-x))

#Exact Solution

def u(x, t): return 8*np.sin(np.pi*x)*np.exp(-t*np.pi**2)/np.pi**3


J = 24;  dx = 1.0 / J;  x = np.linspace(0, 1, J+1)
T = 0.1; N = 24;  dt = T / N; mu = dt / dx**2

Uold = u0(x[1:J]);  Unew = np.zeros(J-1)

# Build the matrices A and B

a = (-mu/2)*np.ones(J-2);  b = (1+mu)*np.ones(J-1);
A = np.diag(a, -1) + np.diag(b, 0) + np.diag(a, 1)

a = (mu/2)*np.ones(J-2);  b = (1-mu)*np.ones(J-1);
B = np.diag(a, -1) + np.diag(b, 0) + np.diag(a, 1)

# Time stepping

for n in range(N):
	Unew = np.linalg.solve(A, B.dot(Uold))
	for j in range(J-1):
		Uold[j] = Unew[j]
	print(Unew)