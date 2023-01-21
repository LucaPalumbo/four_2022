import numpy as np
import matplotlib.pyplot as plt

ft = 212.23
def guadagno(f):
    return 1 / np.sqrt( 1 + (f/ft)**2 ) 


f,s_f, V_in, s_V_in, V_out, s_V_out = np.loadtxt("data.txt", unpack=True, comments='#')
print(f"{f=}")
print(f"{V_in=}")
print(f"{V_out=}")


G_experimental = V_out / V_in
s_G_experimental = np.sqrt( (s_V_in/V_in)**2 + (s_V_out/V_out)**2 )

x = np.logspace(1.5 ,4, 500)
G_simulation = guadagno(x)

plt.xlabel("frequenze [hz]")
plt.ylabel("Guadagno")
plt.grid(linestyle='dashed')
plt.plot(x,G_simulation, label = "simulazione")

plt.errorbar(f,G_experimental,s_G_experimental,s_f, fmt='.', label='dati sperimentali')
plt.xscale('log')
plt.legend()
plt.show()