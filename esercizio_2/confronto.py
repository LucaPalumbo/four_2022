import matplotlib.pyplot as plt
import numpy as np

"""
Migliorare l'accordo tra simulazione e esperimento:
- aggiungere offset di fase di pigreco
- sommare valore costante pari al valor medio su un periodo
- moltiplicare per un fattore di scala (desunto da dati a basse frequenze)
- modificare la frequenza di taglio entro una sigma di incertezza
"""

frequency_quadra = 165.29
period = 1/frequency_quadra
terms = 1000
frequency_taglio = 23  


t=np.linspace(0, period*2 , 1000,endpoint=False) 
bn = lambda n: (2*(1-np.cos(n*np.pi)))/(np.pi* n)
dphi = lambda n: np.arctan( -frequency_quadra * n / frequency_taglio )
Gk = lambda n: 1 / np.sqrt( 1+ (frequency_quadra*n / frequency_taglio)**2 )
s = 1800 * sum( bn(k)*Gk(k)*np.sin(2*np.pi*frequency_quadra*k* t + dphi(k) + np.pi) for k in range (1,terms+1)) + 420


with open('onda_squalo_rinominata/165_29.txt', 'r') as f:
    data = f.readlines()
x = np.array([float(point.split(' ')[0]) for point in data])
y = np.array([float(point.split(' ')[1]) for point in data])

x = x/1e6
plt.title(f"f = {frequency_quadra} Hz")
sigmas = np.ones_like(x)
plt.errorbar(x,y,sigmas,sigmas / 1e6, label="dati", fmt='+')
plt.plot(t,s,label="simulazione")
plt.xlabel("Tempo [s]")
plt.ylabel("Ampiezza [u.a.]")
plt.legend()
#plt.show()
plt.savefig("images/confronto_8.png")