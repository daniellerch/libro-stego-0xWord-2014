import matplotlib.pyplot as plt
import numpy as np

n = 2 ** 10 # Numero de intervalos
Fs = 3000.0 # Hz
dt = 1/Fs   #puntos por periodo

t = np.linspace(0, (n - 1) * dt, n) # Intervalo de tiempo en segundos
y = 0.7 * np.sin(2 * np.pi * 50 * t) +np.sin(2 * np.pi * 120 * t) # Senal

for i in range(0,n):         #introduccion de ruido en la senal
   y[i]=y[i]+0.6*np.random.sample()-0.3

plt.plot(t, y)  #representacion de la senal
plt.plot(t, y, 'ko')
plt.xlabel('Tiempo (s)')
plt.ylabel('$y(t)$')
plt.ylim(-2, 2)
plt.xlim(0,0.05)
plt.show()


Y = np.fft.fft(y)/n # transformada de Fourier Normalizada
freq = np.fft.fftfreq(n, dt) # Recuperamos las frecuencias de la FFT

plt.vlines(freq, 0, 2*abs(Y)) # Representamos

plt.vlines(0,-1,1)
for i in range(2,10,2):
    plt.hlines(float(i)/10,-2.5,2.5)

#ejes grafica
plt.ylim(0, 1)
plt.xlim(-200,200)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud($Y$)')
plt.show()

