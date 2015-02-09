# Visual representation of pseudo-random algorithm that was never 
# actully random. If the 3-D plane is shifted appropiatly the pattern 
# becomes clear.
#
# Need to have 'triples.dat' file
#
# AMS

import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import Axes3D, axes3d
from matplotlib import cm
from pylab import show
from numpy import *

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111, projection='3d')
allpoints=loadtxt('triples.dat')
xpoints=allpoints[:,0]
ypoints=allpoints[:,1]
zpoints=allpoints[:,2]
ax.scatter(xpoints,ypoints,zpoints, c='g', s=1, marker='o') # c sets the color, s is the marker size, marker is the marker type
show()

