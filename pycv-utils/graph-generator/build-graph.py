import os.path


for algo in "./algorithms":
	exec algo > ( "./graphs/" + algo + ".json" )