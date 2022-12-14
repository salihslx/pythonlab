import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,3*np.pi,1000)
plt.subplot(1,2,1)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel('angle')
plt.ylabel('sin(x)')

plt.title('wavw formof sin function',color = 'b')
plt.grid()
plt.subplot(1,2,2)
z = np.cos(x)
plt.plot(z)
plt.xlabel('angle')
plt.ylabel('cos(x)')
plt.plot(z,color ='r')
plt.title("wave form of cos function", color='b')
plt.legend()
plt.grid()
plt.show()