import sys
from PIL import Image

# Leemos la imagen pasada como parametro
i = Image.open(sys.argv[1]) 
pixels = i.load()
width, height = i.size

# Recorremos la imagen calculando el histograma
histogram = [0]*255
for y in range(height):
	for x in range(width):
		cur_pixel = pixels[x, y]
		histogram[cur_pixel]+=1

# Restamos las parejas de barras
total=0
for y in xrange(1, len(histogram), 2):
	dif=abs(histogram[y-1]-histogram[y])
	total+=dif

print total

