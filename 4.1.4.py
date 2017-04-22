import sys
from scikits.audiolab import wavread, wavwrite

mensaje_oculto = "mensaje que se va a ocultar en el fichero de audio, mensaje que se va a ocultar en el fichero de audio, mensaje que se va a ocultar en el fichero de audio, mensaje que se va a ocultar en el fichero de audio, mensaje que se va a ocultar en el fichero de audio"

mensaje_bin = ""

a1=0
data_img=[]

#Se carga en la variable data las muestras de la cancion
#que se pasa por parametro en el comanda
data, sample_frequency, encoding = wavread(sys.argv[1])
data_LSB=data

#Conversion del mensaje oculto en formato texto a binario,
#Se completa por delante de 0 para obtener 8 bits completos
#por cada caracter.
for i in range (0,len(mensaje_oculto)):
    a2 = bin(ord(mensaje_oculto[i]))
    if len(a2)== 9: mensaje_bin += '0'
    if len(a2)== 8:
        mensaje_bin += '0'
        mensaje_bin += '0'        
    if len(a2)== 7:
        mensaje_bin += '0'
        mensaje_bin += '0'
        mensaje_bin += '0'        
    for j in range (2,len(a2)):
        mensaje_bin = mensaje_bin + a2[j]

#Insercion de cada bit del mensaje en el LSB de cada muestra.
#Se inserta hasta el final del mensaje.
for i in range(0, len(data)):
    for j in range(0, 2):
        b=data[i][j]*32768+32768
        f=(int(b)>>1)<<1

        # insertamos un 0 o 1 en las muestras
        c=f^(int(mensaje_bin[a1]))
              
        g=(float(c)-32768)/32768
        data_LSB[i][j] = g
        a1+=1
        if a1 >= len(mensaje_bin):
            break
    if a1 >= len(mensaje_bin):
        break

#salvamos el fichero marcado
filename2= "audio_mark.wav"
wavwrite(data_LSB,filename2,sample_frequency,encoding)

