import numpy as np

# Initial conditon

def u0(x): return (x*(1-x))

#Exact Solution

def u(x, t): return 8*np.sin(np.pi*x)*np.exp(-t*np.pi**2)/np.pi**3

# Discretization parameters

J = 24;  dx = 1.0 / J;  x = np.linspace(0, 1, J+1)
T = 0.1;  N = 24;  dt = T / N;  mu = dt / dx**2
theta =1./2

# Build the system matrix

a = (1-theta)*mu*np.ones(J-2);  b = (1-2*(1-theta)*mu)*np.ones(J-1); #theta=1/2 a = 1/2*np one
A = np.diag(a, -1) + np.diag(b, 0) + np.diag(a, 1)

c = -(theta*mu)*np.ones(J-2);  d = (1+2*theta*mu)*np.ones(J-1);
B = np.diag(c, -1) + np.diag(d, 0) + np.diag(c, 1)

# Initialize the solution vectors

Uold = u0(x[1:J]);  Unew = np.zeros(J-1)

# Time stepping
#B*Unew = A*Uold

for n in range(N):
    Unew = np.linalg.solve(B, A.dot(Uold))
    for j in range(J-1):
         Uold[j] = Unew[j]
    print(Unew)
