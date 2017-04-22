import sys
from scikits.audiolab import wavread, wavwrite
from PIL import Image

data, sample_frequency, encoding = wavread(sys.argv[1])
data_LSB=data
data_img=[]

img = Image.new("1",(8*10,2*len(data)/(8*10)+1))

# Establecemos valores para LSB=1 y LSB=0
for x in range(0,len(data)):
   for y in range(0,2):
      m=0
      f=data_LSB[x][y]*32768+32768
      if int(f)%2==0: m=0
      else: m=255
      data_img += [m]

img.putdata(data_img)
img.show()
