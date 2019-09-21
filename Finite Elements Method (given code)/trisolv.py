'''
Code given from professor Michael Plexousakis, instructor of the course.
http://users.tem.uoc.gr/~plex/mem253-Fall2017/
'''
import numpy as np

def trislv(d, e, f, b):
	"""
	Solve the tridiagonal system

	[ d1    f1                          ] [     x_1 ]   [     b_1 ]
	[ e2    d2    f2                    ] [     x_2 ]   [     b_2 ]
	[       ..    ..   ..               ] [     ... ] = [     ... ]
	[         e_{N-1}  d_{N-1}  f_{N-1} ] [ x_{N-1} ]   [ b_{N-1} ]
        [	               e_N      d_N ] [     x_N ]   [     b_N ]
	"""
	n = b.size
	x = np.zeros(n)

	for i in range(1,n):
		e[i] = e[i] / d[i-1]
		d[i] = d[i] - f[i-1] * e[i]

	for i in range(1,n):
		b[i] = b[i] - e[i] * b[i-1]

	x[n-1] = b[n-1] / d[n-1]
	for i in range(n-2,-1,-1):
		x[i] = (b[i] - f[i] * x[i+1]) / d[i]

	return x

# Test the solution algorithm

if __name__ ==  "__main__":
	n = 20

	d =    4*np.ones(n)
	e = (-1)*np.ones(n)
	f = (-1)*np.ones(n)

	b = np.ones(n)
	x = trislv(d, e, f, b)

# Compare with solve from numpy.linalg

	d =    4*np.ones(n);
	e = (-1)*np.ones(n-1)
	A = np.diag(e, -1) + np.diag(d, 0) + np.diag(e, 1)

	b = np.ones(n)
	y = np.linalg.solve(A,b)

	for j in range(n): print("x[%2d] = %f  y[%2d] = %f  Error = %e" % (j, x[j], j, y[j], abs(x[j]-y[j])))
