import matplotlib.pyplot as plt
import numpy as np

frequency_quadra = 29.28
period = 1/frequency_quadra
amplitude = 1024 # ?
terms = 100
frequency_taglio = 23  


t=np.linspace(0, period*2   , 1000,endpoint=False) 
bn = lambda n: (2*(1-np.cos(n*np.pi)))/(np.pi* n)
dphi = lambda n: np.arctan( -frequency_quadra * n / frequency_taglio )
Gk = lambda n: 1 / np.sqrt( 1+ (frequency_quadra*n / frequency_taglio)**2 )
s = sum( bn(k)*Gk(k)*np.sin(2*np.pi*frequency_quadra*k* t + dphi(k) + np.pi) for k in range (1,terms+1)) 

s = s*512 +440

with open('onda_squalo_rinominata/29_28.txt', 'r') as f:
    data = f.readlines()
x = np.array([float(point.split(' ')[0]) for point in data])
y = np.array([float(point.split(' ')[1]) for point in data])

x = x/1e6
plt.plot(x,y, label="dati")
plt.plot(t,s,label="simulazione")
plt.show()