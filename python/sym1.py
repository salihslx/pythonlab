
import sys
import numpy as np
from matplotlib.pyplot import*
matplotlib.use('agg')

x = np.linspace(0,2,10)
y = x**2
z = x**3

plot(x,x,label='linear')
stem(x,y,label='quadratic',use_line_collection =True)

plot(x,z,label ='cubic')

xlabel('x label')
ylabel('y label')

title("simple plot")
axis([0,2,0,5])
legend() 
savefig(sys.stdout.buffer)
sys.stdout.flush()
