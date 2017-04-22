import sys
from PIL import Image

# Leemos la imagen pasada como parametro
i = Image.open(sys.argv[1]) 
pixels = i.load()
width, height = i.size

# Recorremos la imagen guardando los colores diferentes
colors = {}
for y in range(height):
	for x in range(width):
		pixel = pixels[x, y]
		colors[pixel] = colors.get(pixel, 0) + 1

# Contamos los colores
count = 0
for y in colors:
	count+=1

print count

