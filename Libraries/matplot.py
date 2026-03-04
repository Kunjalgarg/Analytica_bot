import matplotlib.pyplot as plt
import numpy as np
x= np.array([0,5,1])
y= np.array([0,250,2])

##plt.plot(x,y,'o')
##plt.plot(x,y, marker='o')
##plt.subplot(x,'*:r')
##plt.plot(y,'o-c')
##plt.plot(x,y, linestyle='dotted')
plt.pie(x)
plt.grid()
plt.show()
