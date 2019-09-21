'''
Code given from professor Michael Plexousakis, instructor of the course.
http://users.tem.uoc.gr/~plex/mem253-Fall2017/
'''
import numpy as np
import gaussQuad as gq
import matplotlib.pyplot as plt

# Finite element method to solve the two-point boundary value problem
#
#    -u'' + q u = f,  in [l, r]
#
# with zero Dirichlet boundary condtions.

# The functions q and f

def q(x): return 1+x**2
def f(x): return 2-np.exp(x)

# Endpoints and partition of [l,r]

l = 0.0;  r = 1.0;  N = 99;  h = (r - l) / (N+1);  x = np.linspace(l, r, N+2)

# The system matrix is tridiagonal symmetric positive definite. Compute the
# main diagonal and the first diagonal above. Use a Gauss quadrature rule
# exact for polynomials of degree <= 4

nq, p, w = gq.gaussQuad(4)

d = np.zeros(N)
c = np.zeros(N)

for j in range(N+1):
	xj = x[j];  s1 = 0.0;  s2 = 0.0;  s3 = 0.0
	for k in range(nq):
		qk = q(xj + h*p[k])
		s1 += w[k] * qk * (1 - p[k])**2
		s2 += w[k] * qk * (1 - p[k])*p[k]
		s3 += w[k] * qk *      p[k] *p[k]

	if j > 0:           d[j-1] += h * s1
	if j > 0 and j < N: c[j-1] += h * s2
	if j < N:           d[j  ] += h * s3

for j in range(N):
	d[j] += 2 / h
	c[j] -= 1 / h

# Use a Gauss quadrature rule exact for polynomials of degree <= 5

b = np.zeros(N)
nq, p, w = gq.gaussQuad(5)

for j in range(N+1):
	xj = x[j];  s1 = 0.0;  s2 = 0.0
	for k in range(nq):
		fk = f(xj + h*p[k])
		s1 += w[k] * fk * (1 - p[k])
		s2 += w[k] * fk *      p[k] 

	if j > 0: b[j-1] += h * s1
	if j < N: b[j  ] += h * s2

# Solve the system

for k in range(1,N):
	t = c[k-1] / d[k-1]
	d[k] -= t * c[k-1]
	b[k] -= t * b[k-1]

b[N-1] = b[N-1] / d[N-1]
for k in range(N-2, -1, -1):
	b[k] = (b[k] - c[k] * b[k+1]) / d[k]

# Plot the solution

u = np.lib.pad(b, (1,1), 'constant', constant_values=(0, 0))
plt.plot(x, u, 'k-')
plt.legend(('u'), loc='upper right', shadow=True)
plt.show()
