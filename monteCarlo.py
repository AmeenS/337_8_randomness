# Fucntion to determine area of 2+cos(t*theta), or any closed shape,
# using Monte Carlo method.
#
#
#
# AMS

"""
from numpy import *

def ff():
	n = 1.e7			# Number of positions
	a = 3.					# Greatest value of function
	x = 6.*random.rand(n) - a # Normalization of x and y so range that 
	y = 6.*random.rand(n) - a # range and domain cover entirety of shape
	r = sqrt(y**2 + x**2)		#conversion into polar coordinates
	theta = arctan2(y,x)

	k = r<= 2 + cos(7*theta)
	l = sum(k)
	print l/float(n) * (2*a)**2
	print 9*pi/2.
ff()
"""
from numpy import *
n = 1000000
u = random.rand(n)
v = random.rand(n)
x = 6*u - 3
y = 6*v - 3
r = sqrt(x**2 + y**2)
theta = arctan2(y,x)
a = zeros(n)

a[r <=  2 + cos(7*theta)] = 1

print 36*sum(a)/n
