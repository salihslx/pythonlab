import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

t = np.linspace(0,1,100)

y = np.sin(2*np.pi*t)  

dat = [t,y]
type(dat)
df = pd.DataFrame(data=dat, index=["Time","Amplitude"]).T
print(df)

df = pd.DataFrame(data=dat, index=["Time","Amplitude"]).T

df.to_csv('data.csv')

df1 = pd.read_csv('data.csv',index_col=0)

df1.plot(x="Time",y="Amplitude")

plt.show()  

df1.hist(column = "Amplitude")

plt.show()

print('Standard Deviation')

print(df1.std(0))

print("Mean")
print(df1.mean(0))
  