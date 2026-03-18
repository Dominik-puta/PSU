import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)
x = data[:,0]
y = data[:,3]
wt = data[:,5]
print(x.min(), x.max(), np.average(x))
plt.scatter(x,y,s=wt)
plt.axis([0,50,0,200])
plt.xlabel('mpg')
plt.ylabel('hp')
plt.title('Auti')
plt.show()