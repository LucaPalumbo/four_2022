import matplotlib.pyplot as plt
import numpy as np

duty_cycle = 0.25

#frequency_taglio = 23  
#frequency = 165.29
#frequency = frequency_taglio * 20
#period = 1/frequency

frequency_taglio = 23
periodo_caratteristico = 1/frequency_taglio
periodo = periodo_caratteristico / 16

omega = (1/periodo) * 2 * np.pi


t=np.linspace(0, periodo*10, 1000 ,endpoint=False) 

def G(k):
    return 1 / np.sqrt( 1+( omega * k / (2*np.pi*frequency_taglio))**2 )

def phi(k):
    return np.arctan( (-omega * k) / (2*np.pi*frequency_taglio) )


g = duty_cycle + sum([ 2/(k*np.pi) * np.sin(k*np.pi*duty_cycle)*np.cos(omega*k*t )  for k in range(1,1000) ])
g_integrato =  duty_cycle + sum([ G(k)* 2/(k*np.pi) * np.sin(k*np.pi*duty_cycle)*np.cos(omega*k*t + phi(k) )  for k in range(1,1000) ])


plt.plot(t,g, label="non integrato")
plt.plot(t,g_integrato, label="integrato")
plt.legend()
plt.show()