import matplotlib.pyplot as plt
import numpy as np


frequency_quadra = 165.29
period = 1/frequency_quadra
amplitude = 1024
terms = 10
frequency_taglio = 23  # unknown


t=np.linspace(0, period*4, 1000,endpoint=False) 


bn = lambda n: (2.*(1-np.cos(n*np.pi)))/(np.pi* n)

dphi = lambda n: np.arctan( -frequency_quadra * n / frequency_taglio )

Gk = lambda n: 1 / np.sqrt( 1+ (frequency_quadra*n / frequency_taglio)**2 )

s = sum( bn(k)*Gk(k)*np.sin(2*np.pi*frequency_quadra*k* t + dphi(k)) for k in range (1,terms+1)) 


t = t/period
plt.plot(t,s,label=f"Serie di Fourier [n={terms}]")
plt.xlabel("Tempo [T]")
plt.ylabel("Ampiezza [u.a.]")


# Plot the data
#plt.plot(x, y)
plt.show()