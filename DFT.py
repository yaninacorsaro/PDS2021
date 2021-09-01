# -*- coding: utf-8 -*-
"""
@author: Yanina Corsaro
"""

import numpy as np
import matplotlib.pyplot as plt
from sen import mi_funcion_sen
from scipy.fftpack import fft, fftfreq
from funcionDFT import mi_funcion_DFT

N  = 100 # muestras
fs = 100 # Hz
a0 = 1       # Volts
p0 = np.pi/4  # radianes
f0 = 10    # Hz
dt = 1/(fs)

tt, y= mi_funcion_sen( vmax=a0 , dc=0 , ff=f0 , ph=p0, nn=N , fs=fs )


fft = fft(y)
fftabs=np.abs(fft)
fftangle=np.angle(fft)

frq, XX = mi_funcion_DFT( y, N, fs  )
  
xfabs=np.abs(XX)
xfangle=np.angle(XX)


# grafico módulo de la dft
fig, (ax, ax1) = plt.subplots(1, 2)
ax.plot(frq, xfabs, "-", frq, fftabs, ":")
ax.set(xlabel='frecuencia', ylabel='módulo',title='DFT módulo')
ax.grid()
plt.show()

ax1.plot(frq, xfangle, "-", frq, fftangle, ":")
ax1.set(xlabel='frecuencia', ylabel='fase',title='DFT fase')
ax1.grid()
plt.show()

fig, ax = plt.subplots()
ax.plot(tt, y)
ax.set(xlabel='tiempo (segundos)', ylabel='amplitud (V)',title='señal: senoidal')
ax.grid()
plt.show()








