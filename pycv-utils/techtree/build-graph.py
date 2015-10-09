from os import listdir
from os.path import isdir
import importlib
import json
import sys


dirname = "../../experiments/"

print 'Graph builder start running... looking for algorithms in ' + dirname
for algorithm in listdir('algorithms'):
	#buildTree = getattr(algorithm, 'main'
	if isdir("algorithms/" + algorithm):
		m = importlib.import_module("algorithms." + algorithm + ".main") 
		print 'Algorithm \"' + algorithm + '\" found, start running...',
		b = m.main(dirname)
		
		jsonname = "graphs/" + algorithm + ".json"
		print 'done. Save to', jsonname
		with open(jsonname, 'w') as f:
			f.write(b.graph)

with open("algorithms.json", 'w') as f:
	f.write( json.dumps([i for i in listdir('algorithms') if isdir("algorithms/" + i)] ))

