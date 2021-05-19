import numpy as np
import matplotlib.pyplot as plt
array1 = np.arange(0,3)
array2 = [0,52,85,63,32]
array3 = np.array([65,52,96,75])
array4 = ([12,52,85,63],[15,5,857,53])
array5 = np.array([[20,25,56],[34,78,90]])
x = np.ones(5)
y = np.zeros(5)
z = np.linspace(0,1,5)
t = np.mean(array5,(0,1))
m = np.average(array5[:])
print(array5)
a = np.reshape(array5,6)
print(t)
print(a.shape)
print(a[0])
print(m)
plt.plot(z,array2, 'b')
plt.show()

