import sys
from scikits.audiolab import wavread, wavwrite
import matplotlib.pyplot as plt
import numpy as np


# carga del fichero de audio
data, sample_frequency, encoding = wavread(sys.argv[1])
dt = 1.0/sample_frequency
    
# obtencon del espectro
n = len(data)
if (len(data.shape) > 1): # stereo
    monoData = [];
    for i in range(len(data)):
        monoData.append((data[i][0] + data[i][1])/2)
    Y = np.fft.fft(monoData) / n
 else: # mono
    Y = np.fft.fft(data) / n

freq = np.fft.fftfreq(n, dt) # Recuperamos las frecuencias de la FFT

plt.vlines(freq, 0, 2*abs(Y)) # Representamos

plt.vlines(0,-1,1)
for i in range(2,18,2):
    plt.hlines(float(i)/1000,-12,12)

#ejes grafica
plt.ylim(0, 0.018)
plt.xlim(-1000,1000)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud($Y$)')
plt.show()
