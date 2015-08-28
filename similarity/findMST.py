import networkx as nx
import matplotlib.pyplot as plt

def findMST(simList):
	g = createDistanceGraph(simList)
	mst = nx.minimum_spanning_tree(g)
	print mst.edges()
	print mst.nodes()
	nx.draw_networkx(mst, with_labels = True)


	plt.show()


def createDistanceGraph(simList):
	G = nx.Graph()
	for sim, x1, x2 in simList:
		distance = 1.0 / sim
		G.add_edge(x1, x2, weight = distance)
	return G


if __name__ == "__main__":
	import analysis
	experiments_folder = "../experiments/"
	corpus = analysis.makeCorpus(experiments_folder)

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
		  similarity = analysis.expSimilarity(corpus[n1], corpus[n2])
		  # [TODO] should be write into a file such as relation.json in future
		  # print to stdout is now for testing only
		  simList.append((similarity, n1, n2))
		  print '%0.5f,%s,%s' % (similarity, n1, n2)

	findMST(simList)