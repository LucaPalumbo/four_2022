import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as spi
from scipy.signal import square
A=1.
T=2.
a0=0
omega=2.*np.pi/T
terms=100

t=np.linspace(-0.05,T+0.05,1000,endpoint=False)
n=list(range(1,1000,2))

an=lambda n: (2/(np.pi*n))**2

s= a0/2 +sum( an(k)*np.cos(k*omega*t) for k in range(1,terms*1) if k%2!=0)

plt.plot(t,s,label=f"Serie di Fourier [n={terms}]")
plt.xlabel("tempo [t]")
plt.ylabel("y=f(t) [u.a]")
plt.legend(loc='best',prop={'size':10})
plt.title("simulazione onda quadra")
plt.show()