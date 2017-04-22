import sys
from PIL import Image

# Leemos la imagen pasada como parametro
i = Image.open(sys.argv[1]) 
pixels = i.load()
width, height = i.size

# Establecemos valores para LSB=1 y LSB=0
for y in range(height):
	for x in range(width):
		if pixels[x, y]%2==1:
			pixels[x, y] = 0
		else:
			pixels[x, y] = 255

i.show()
i.save(sys.argv[2])

