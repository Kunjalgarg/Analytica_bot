import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numpy import random

arr= np.array([2,1,4,3])

##print(random.rand(3,5))
##print(random.rand(5))

##print(random.randint(50))
##print(random.randint(10,size=(3,5)))

##print(random.choice(arr, p=[0.1,0.3,0.6,0], size=(3,5)))

##random.shuffle(arr)
##print(arr)

##print(random.permutation(arr))

##sns.displot(arr)
sns.displot(arr,kind='kde')
plt.show()
