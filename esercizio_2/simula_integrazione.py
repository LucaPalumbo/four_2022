import matplotlib.pyplot as plt
import numpy as np


frequency_quadra = 28.29
period = 1/frequency_quadra
amplitude = 1
terms = 1000
frequency_taglio = 23  


t=np.linspace(0, period*4, 1000,endpoint=False) 


bn = lambda n: (2.*(1-np.cos(n*np.pi)))/(np.pi* n)

dphi = lambda n: np.arctan( -frequency_quadra * n / frequency_taglio )

Gk = lambda n: 1 / np.sqrt( 1+ (frequency_quadra*n / frequency_taglio)**2 )

s = sum( bn(k)*Gk(k)*np.sin(2*np.pi*frequency_quadra*k* t + dphi(k)) for k in range (1,terms+1)) 


t = t/period
plt.plot(t,s,label=f"Simulazione [f={frequency_quadra}]")
plt.xlabel("Tempo [T]")
plt.ylabel("Ampiezza [u.a.]")
plt.legend(loc = "lower left")

#plt.savefig("/home/luca/Documents/universita/lab2/four_2022/esercizio_2/images/sim_8.png")
# Plot the data
plt.plot(t, s)
plt.show()