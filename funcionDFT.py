"""

@author: Yanina Corsaro
"""

import numpy as np

def mi_funcion_DFT( y, N, fs  ):
    
    def twiddle_factor(k, n, N):
        Wk = np.cos(2*np.pi*k*n/N ) - np.sin(2*np.pi*k*n/N)*1j
        return Wk
    frq = np.linspace( start= 0, stop= fs ,num = N)    
    dft = []
    for k in range(0,N):
        res = 0
        for n in range(0,N):
            res = res + twiddle_factor(k, n, N)*y[n]
        dft.append(res) 
    dft = np.array(dft)       
    return frq, dft










