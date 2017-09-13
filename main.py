import numpy as np 
import matplotlib.pylab as plt 
def f(y):
    return 2* np.cos(y) + 2015
y1 = np.arange(0.0,5.0,0.1)
plt.plot(y1, f(y1),'bo', y1, f(y1), 'g--')
plt.savefig('p1.png')

plt.show()
  
