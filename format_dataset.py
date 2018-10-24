import json,pickle

data = None

with open("colorsdataset.json","r") as f:
	data = json.loads(f.read())

colormap = dict()

def hex_to_rgb(hex):
	return (16 * int(hex[i],16) + int(hex[i+1],16) for i in (1,3,5))


def mapper(color_obj):
	r,g,b = hex_to_rgb(color_obj["hex"])
	return (color_obj["color"],r,g,b)

data = list(map(mapper,data["colors"]))

with open("cleanedColorDataset.pickle","wb") as f:
	pickle.dump(data,f)