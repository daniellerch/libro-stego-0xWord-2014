import sys
import numpy
from PIL import Image
from scipy import stats

f = open(sys.argv[1], "r" )
coef = []
for line in f:
    coef.append(int(line))

# Primero usamos el 1% del total de coefientes DCT,
# despues el 2% y asi sucesivamente
last_pval=0
l=0
for sz in range(1,100):
	histogram = [0]*256

	# Usamos solo el porcentaje de coef que indica sz
	l=int(len(coef)*(float(sz)/100))
	y=coef[1:l]
	for v in y:
		idx=v+128

		if idx>=256 or idx<=0:
			continue

		histogram[idx]=histogram[idx]+1

	# Obtenemos las barras pares e impares
	obs = numpy.array([])
	exp = numpy.array([])

	for y in range(1, len(histogram)/2):
		x=histogram[128-y]
		z=(histogram[128-y]+histogram[128+y])/2

		if x>0 and z>0:
			obs = numpy.append(obs, [x])
			exp = numpy.append(exp, [z])

	# Calculamos chi square y p-value
	chi,pval = stats.chisquare(obs, exp)
	pval = 1-pval

	if pval<=0.01:
		if last_pval==0:
			print "Cover"
			exit()
		else:
			print last_pval
			break

	last_pval=pval;

print "Stego, longitud aproximada del mensaje: %d%%" % sz



