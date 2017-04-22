import sys

fin=open(sys.argv[1], 'r')

lines = fin.readlines()

i=0
for l in lines:
	features=l.split(' ');
	string=""
	if sys.argv[2] in features[len(features)-1]:
		string='1 '
	else:
		string='0 '

	i=0
	features.pop()
	for field in features:
		string+= str(i)+':'+field+' '
		i+=1
	print string




