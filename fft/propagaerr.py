import uncertainties as un
from uncertainties.umath import *
import numpy as np

L = 0.5
def omega( C):
    return 1 / sqrt(L * C)

def propagate_error():
    C = un.ufloat(0.22e-6, 0.22e-6 * 0.1 )
    w = omega(C)
    print(w)
    f = w / (2*np.pi)
    print(f)

propagate_error()