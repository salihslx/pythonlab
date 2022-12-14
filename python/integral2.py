import scipy.integrate
import  sympy as sp
x = sp.symbols('x')
f = sp.integrate(sp.exp(-x**2))

print('value of f :',f)