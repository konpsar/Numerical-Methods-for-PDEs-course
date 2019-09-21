import numpy as np

# Initial conditon

def u0(x): return (x*(1-x))

#Exact Solution

def u(x, t): return 8*np.sin(np.pi*x)*np.exp(-t*np.pi**2)/np.pi**3

def max_error(U, exact):
    tmp = abs(U-exact)
    return np.max(tmp)

#u(0.1)

# Discretization parameters

hh = np.array([0.1, 0.05])
J = np.power(hh, -1);  #h=dx = 1.0 / J;  
x = np.array([[np.linspace(0, 1, J[0]+1)], [np.linspace(0, 1, J[1]+1)])
kk = np.array([[(1/2)*np.power(hh, 2)], [(5*np.power(hh, 2)]]) ; #1/2* h^2 
mmu = kk / np.power(hh, 2)
ttheta =np.array([1/2, 3/4, 1])

#for theta in ttheta:
#    for mu in mmu:

#Define elements of matrices
a = (1-theta)*mu*np.ones(J-2);  b = (1-2*(1-theta)*mu)*np.ones(J-1);
c = -(theta*mu)*np.ones(J-2);  d = (1+2*theta*mu)*np.ones(J-1);

# Build the system matrices

A = np.diag(a, -1) + np.diag(b, 0) + np.diag(a, 1)
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
	
	
	#import numpy as np
#h = np.array([0.1, 0.05])
#J = np.power(h, -1);  #h=dx = 1.0 / J;  
#x = np.array([[np.linspace(0, 1, J[0]+1)], [np.linspace(0, 1, J[1]+1)]])
#print(h)
#print(J)
#print(x[1, :])
