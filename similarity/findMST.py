import networkx as nx
from networkx.readwrite import json_graph

import matplotlib.pyplot as plt
from analysis import makeCorpus, expSimilarity

experiments_folder = "../temporily-in-a-mess/"


def findMST(simList, plot=False):
	g = createDistanceGraph(simList)
	mst = nx.minimum_spanning_tree(g)
	if plot:
		nx.draw_networkx(mst, with_labels = True)
		plt.show()
	print json_graph.node_link_data(mst)



def createDistanceGraph(simList):
	G = nx.Graph()
	for sim, x1, x2 in simList:
		distance = 1.0 / sim
		G.add_edge(x1, x2, weight = distance)
	return G

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
		  simList.append((similarity, n1, n2))
		  print '%0.5f,%s,%s' % (similarity, n1, n2)
	findMST(simList)

if __name__ == "__main__":
	main()
	