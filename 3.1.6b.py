import sys
import numpy
from PIL import Image
from scipy import stats

# Leemos la imagen pasada como parametro
i = Image.open(sys.argv[1]) 
pixels = i.load()
width, height = i.size
chunk=1024
last_pval=0

# Leemos la imagen a trozos cada vez mas grandes
for sz in xrange(chunk, height*width, chunk):

	# Recorremos la imagen calculando el histograma
	histogram = [0]*255
	for y in range(height):
		if y*height>sz:
			break
		for x in range(width):
			if type(pixels[x,y]) is tuple:
				for k in range(len(pixels[x, y])):
					cur_pixel = pixels[x, y][k]
					histogram[cur_pixel]+=1
			else:
				cur_pixel = pixels[x, y]
				histogram[cur_pixel]+=1

	# Obtenemos las barras pares e impares
	obs = numpy.array([])
	exp = numpy.array([])
	X=0
	for y in xrange(1, len(histogram), 2):
		x=histogram[y-1]
		z=(histogram[y-1]+histogram[y])/2
		if x>0 and z>0:
			obs = numpy.append(obs, [x])
			exp = numpy.append(exp, [z])

	# Calculamos chi square y p-value
	chi,pval = stats.chisquare(obs, exp)

	if pval<=0.01:
		if last_pval==0:
			print "Cover"
			exit()
		else:
			print last_pval
			break

	last_pval=pval;

print "Stego, longitud aproximada del mensaje: %d" % sz

