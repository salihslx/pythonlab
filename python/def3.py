import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
def model(x,t):
    k = 2
    dxdt = -k*x
    
    return dxdt
x0 = 5
t = np.linspace(0,20)

x = odeint(model,x0,t)
plt.plot(t,x,label ='k=2')
plt.title('first order difrential equation response')
plt.xlabel('time')
plt.ylabel('x')
plt.legend()
plt.show()