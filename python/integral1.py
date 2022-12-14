import scipy.integrate
import  sympy as sp
x = sp.symbols('x')
func = lambda x:(x*x+3*x+1)
i = scipy.integrate.quad(func, 0, 1)
print('value of i :',i)