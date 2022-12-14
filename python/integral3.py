import scipy.integrate

import  sympy as sp
x = sp.symbols('x')
func = lambda x:(sp.exp(-x)*(sp.sin(3*x)))
i = scipy.integrate.quad(func, 0,2*sp.pi)
print('value of i :',i)