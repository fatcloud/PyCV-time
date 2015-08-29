import networkx as nx
from networkx.readwrite import json_graph

import matplotlib.pyplot as plt
from analysis import makeCorpus, expSimilarity

experiments_folder = "../experiments/"

def findMST(simList, plot=False):
	g = createDistanceGraph(simList)
	mst = nx.minimum_spanning_tree(g.to_undirected())
	
	el = [e for e in g.edges() if e in mst.edges() or tuple(reversed(e)) in mst.edges()]
	g = nx.DiGraph()
	g.add_edges_from(el)
	if plot:
		nx.draw_networkx(g, with_labels = True)
		plt.show()
	print json_graph.node_link_data(g)


def createDistanceGraph(simList):
	G = nx.DiGraph()
	for sim, dep, x1, x2 in simList:
		distance = 1.0 / sim
		if dep == 0: 
			G.add_edge(x1, x2, weight = distance)
		else:
			G.add_edge(x2, x1, weight = distance)
	return G

def expDependency(exp1, exp2):
	""" calculate the direction of dependence of 2 experiments 
		return 0 if exp1 is considered parent of exp2, otherwise return 1
	"""
	words1, _ = exp1
	words2, _ = exp2
	l1 = len(words1)
	l2 = len(words2)
	l_intersect = len(set(words1).intersection(set(words2)))
	return 0 if l_intersect / float(l1) >= l_intersect / float(l2) else 1

def main():
	corpus = makeCorpus(experiments_folder)
	exps = corpus.keys()
	N = len(corpus)

	simList = []
	for idx, exp in enumerate(exps):
		if idx == N-1:
		  break
		# calculate pair similarity
		for next_ in range(idx+1, N):
		  n1 = exps[idx]
		  n2 = exps[next_]
		  similarity = expSimilarity(corpus[n1], corpus[n2])
		  # [TODO] should be write into a file such as relation.json in future
		  # print to stdout is now for testing only
		  dep = expDependency(corpus[n1], corpus[n2])
		  simList.append((similarity, dep, n1, n2))
		  # print '%0.5f,%s,%s' % (similarity, n1, n2)
	findMST(simList, False)

if __name__ == "__main__":
	main()
	