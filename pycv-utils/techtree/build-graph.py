from os import listdir
from os.path import isdir
import importlib
import json
import sys

dirname = "../../experiments/"
for algorithm in listdir('algorithms'):
	#buildTree = getattr(algorithm, 'main'
	if isdir("algorithms/" + algorithm):
		m = importlib.import_module("algorithms." + algorithm + ".main") 
		b = m.main(dirname)
		with open("graphs/" + algorithm + ".json", 'w') as f:
			f.write(b.graph)

with open("algorithms.json", 'w') as f:
	f.write( json.dumps([i for i in listdir('algorithms') if isdir("algorithms/" + i)] ))