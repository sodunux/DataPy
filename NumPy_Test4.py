import numpy as np 
from pylab import *
n=12
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
for x,y in zip(X,Y1):
	text(x+0.4,y+0.05,'%.2f' %y,ha='center',va='bottom')
	show()