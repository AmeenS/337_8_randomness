# Using random numbers to design a Gaussain distribution
#
# AMS

from numpy import *
from pylab import *
from myhistogram import *
from scipy.special import erfinv

def g(u): return sqrt(2.)*erfinv(2.*u-1.)

#homebrew
u = random.rand(1000000)
#v = g(u)

#built-in
v = random.randn(1000000)

ion()
myhistogram( v, -3., 3., 30)

v = linspace(-3.,3.,200)
p = 1/sqrt(2.*pi)*exp(-v**2/2.)
plot(v,p,'r-', alpha=0.5, linewidth= 4,)


draw()
ioff();
raw_input();
