# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:24:27 2021

@author: LeanYani
"""


from numpy import random
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

y = 7 * random.random_sample(N,)

tt = np.linspace( start= 0, stop= (N-1)/fs ,num = N)

# calculo dft con la funcion de scipy
fft = fft(y)
fftabs=np.abs(fft)
fftangle=np.angle(fft)

# calculo dft con mi funcion
frq, XX = mi_funcion_DFT( y, N, fs  )  
xfabs=np.abs(XX)
xfangle=np.angle(XX)


# grafico módulo de la dft, de mi función en rayitas y de la fft punteada
fig, ax = plt.subplots()
ax.plot(frq, xfabs, "-", frq, fftabs, ":")
ax.set(xlabel='frecuencia', ylabel='módulo',title='DFT módulo')
ax.grid()
plt.show()

# grafico fase de la dft, de mi función en rayitas y de la fft punteada
fig, ax1 = plt.subplots()
ax1.plot(frq, xfangle, "-", frq, fftangle, ":")
ax1.set(xlabel='frecuencia', ylabel='fase',title='DFT fase')
ax1.grid()
plt.xlim(0, 100)
plt.ylim(-5, 5)
plt.show()

# grafico la señal senoidal que fue analizada
fig, ax = plt.subplots()
ax.plot(tt, y)
ax.set(xlabel='tiempo (segundos)', ylabel='amplitud (V)',title='señal: aleatoria')
ax.grid()
plt.show()