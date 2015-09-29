import networkx as nx
import json
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt

#from makeCorp import makeCorpus

def buildGraph(simList, plot=False):
	g = distanceGraph(simList)
	trim(g, 0.15)

	#mst = nx.minimum_spanning_tree(g.to_undirected())
	#el = [(i, o, w) for (i, o, w) in g.edges_iter(data=True)  
	#                    if (i, o) in mst.edges() 
	#        			or (o, i) in mst.edges()]
	#g = nx.DiGraph()
	#g.add_edges_from(el)
	if plot:
		nx.draw_networkx(g, with_labels = True)
		plt.show()
	return json.dumps(json_graph.node_link_data(g))
	
def trim(graph, threshold=0.2):
	thr = threshold * graph.size()
	for i, a in enumerate(sorted(nx.to_edgelist(graph), key=(lambda x: x[2]['weight']))):
		if i > thr:
			graph.remove_edge(a[0], a[1])

def distanceGraph(simList):
	G = nx.DiGraph()
	for sim, dep, x1, x2 in simList:
		distance = 1.0 / sim
		if dep == 0: 
			G.add_edge(x1, x2, weight = distance)
		else:
			G.add_edge(x2, x1, weight = distance)
	return G

	