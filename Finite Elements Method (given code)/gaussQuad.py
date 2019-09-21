'''
Code given from professor Michael Plexousakis, instructor of the course.
http://users.tem.uoc.gr/~plex/mem253-Fall2017/
'''


import numpy as np

def gaussQuad(n):
   """
   Return the points and weights of a Gauss quadrature rule on [0, 1] which integrates exactly
   polynomials of degree less than or equal to n
   """
   if n <= 1:
	   return (1, np.array([0.5]), np.array([1.0]))
   elif n <= 3:
	   return (2, np.array([0.2113248654051871, 0.7886751345948129]), np.array([0.5, 0.5]))
   else:
	   return (3, np.array([0.1127016653792583, 0.5, 0.8872983346207417]), np.array([0.2777777777777778, 0.4444444444444444, 0.2777777777777778]))

# Test quadrature rule

if __name__ ==  "__main__":
    def f(x): return x**5 - 2*x**3 + 4*x**2

    n, p, w = gaussQuad(5)
    v = f(p)
    s = np.dot(v, w)
    print("exact integral = %f  approx = %f" % (1.0, s))
