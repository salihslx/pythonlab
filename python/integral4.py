import scipy.integrate
import  sympy as sp
x = sp.symbols('x')
func = lambda x:(sp.exp(-abs(x)))

i = scipy.integrate.quad(func, -3, 3)

print('value of func :',i)