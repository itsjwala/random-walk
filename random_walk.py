import pickle,random,functools,time

data = None

with open("cleanedColorDataset.pickle","rb") as f:
	data = pickle.load(f)


current = ("color name doesn't matter :p",random.randint(0,256),random.randint(0,256),random.randint(0,256))
# current = ("color name doesn't matter :p",30,144,255)

def comparator(a,b):
	d1=d2=0
	for i in (1,2,3):
		d1 += (a[i]-current[i])**2
		d2 += (b[i] - current[i])**2
	return d1 - d2

def nearestColor(color):
	cmp = functools.cmp_to_key(comparator)
	data.sort(key = cmp)
	return data[0]

current = nearestColor(current)
print(current[0])
data = data[1:]

while len(data)>=1:
	nearest = nearestColor(current)
	print(nearest[0])
	current = nearest
	data = data[1:]