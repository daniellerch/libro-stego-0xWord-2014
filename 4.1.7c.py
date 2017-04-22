import sys
from scikits.audiolab import wavread, wavwrite
import numpy as np
import matplotlib.pyplot as plt

outputFilename = "audio-modified.wav"

# funcion para insertar el mensaje en el espectro
# 
def applyModifications(frecuencias):
    mensaje_oculto = "mensaje que se va a ocultar en el fichero de audio, mensaje que se va a ocultar en el fichero de audio"
    mensaje_bin = ""

    #Conversion del mensaje oculto en formato texto a binario,
    #Se completa por delante de 0 para obtener 8 bits completos
    #por cada caracter.
    for i in range (0,len(mensaje_oculto)):
        o=bin(ord(mensaje_oculto[i]))
        if len(o)==9: mensaje_bin += '0'
        if len(o)==8:
            mensaje_bin += '0'
            mensaje_bin += '0'        
        if len(o)==7:
            mensaje_bin += '0'
            mensaje_bin += '0'
            mensaje_bin += '0'        
        for j in range (2,len(o)):
            mensaje_bin= mensaje_bin + o[j]

    for i in range(0,len(mensaje_bin)):
        if int(mensaje_bin[i])==1:
            frecuencias[i*5]=frecuencias[i*5]*5;
    return frecuencias

# funcion para mostrar por pantalla en una figura el espectro
#
def mostrar(freq,Y):
    plt.vlines(freq, 0, 2*abs(Y)) # Representamos
    plt.vlines(0,-1,1)
    for i in range(2,18,2):
        plt.hlines(float(i)/1000,-12,12)
    #ejes grafica
    plt.ylim(0, 0.018)   #.018
    plt.xlim(-5000,5000)  #1000
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud($Y$)')
    plt.show();


# Funcion principal 
#
if __name__ == '__main__':

    # Leemos el fichero WAV (parametro 1) del disco.
    data, fs, enc = wavread(sys.argv[1])
    dt = 1.0/fs 

    # Obtenemos el espectro
    n = len(data)
    print data.shape
    
    if (len(data.shape) > 1): # stereo
        monoData = [];
        for i in range(len(data)):
            monoData.append((data[i][0] + data[i][1])/2)
        Y = np.fft.fft(monoData) / n
    else: # mono
        Y = np.fft.fft(data) / n

    # Recuperamos las frecuencias de la FFT
    freq = np.fft.fftfreq(n, dt) 
      
    # Aplicamos las modificaciones en el espectro
    modSpectrum = applyModifications(Y)
    
    # Transforada inversa para obtener el dominio temporal
    modData = np.real(np.fft.ifft(modSpectrum) * n)
    
    # Se convierte a formato WAV y se graba a disco
    wavwrite(modData, outputFilename, fs)

    # Para mostrar el espectro en pantalla
    mostrar(freq, modSpectrum)

