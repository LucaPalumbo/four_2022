import numpy  as np
import matplotlib.pyplot as plt

f_signal = 23e3 # hz
T_signal = 1/f_signal # s
f_ta = 212 # hz
f_tb = 23590 # hz

terms = 20000
def bn(k):
    return (2 * ( 1 - np.cos(k*np.pi) ) ) / ( np.pi* k) 

def guadagno_A(k):
    return 1 / np.sqrt( 1 + (f_signal*k/f_ta)**2 )

def guadagno_B(k):
    return 1 / np.sqrt( 1 + (f_tb/(f_signal*k))**2 )

def phi_A(k):
    return np.arctan(-f_signal*k / f_ta)

def phi_B(k):
    return np.arctan( f_tb / (f_signal*k) )

t = np.linspace(0,T_signal*2, 1000, endpoint=False)


#s = sum( bn(k)*guadagno_A(k)*np.sin(2*np.pi*f_signal*k* t + phi_A(k) ) for k in range (1,terms+1))

s = sum( bn(k)*guadagno_A(k)*guadagno_B(k)*np.sin(2*np.pi*f_signal*k* t + phi_A(k) + phi_B(k) ) for k in range (1,terms+1))

s = s

plt.plot(t,s, label=f"f = {f_signal} Hz")
plt.legend()
plt.show()