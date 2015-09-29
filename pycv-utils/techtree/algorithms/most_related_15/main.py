from makeCorp import makeCorpus
from similarity_measures import cosine_similarity, jaccard_dependency
from graphs import buildGraph


class BuildTree(object):
    def __init__(self, similarity_func, dependency_func, build_graph_func, folder_name):
        self.similarity_func = similarity_func
        self.dependency_func = dependency_func
        self.build_graph_func = build_graph_func
        self.folder_name = folder_name
        self.run()

    def run(self):
        corpus = makeCorpus(self.folder_name)
        vectors = corpus.keys()
        N = len(corpus)

        simList = []
        for idx, vec in enumerate(vectors):
            if idx == N - 1:
            	break
            # calculate pair similarity
            for next_ in range(idx + 1, N):
                n1 = vectors[idx]
                n2 = vectors[next_]
                # calculate similarity
                similarity = self.similarity_func(corpus[n1], corpus[n2])
                # calculate dependency
                # dependency_func(v1, v2) should return 0 if v1 includes v2
                #                         otherwise return 1
                dep = self.dependency_func(corpus[n1], corpus[n2])
                simList.append((similarity, dep, n1, n2))
                # print '%0.5f,%s,%s' % (similarity, n1, n2)
        self._graph = self.build_graph_func(simList)	


    @property
    def graph(self):
		return self._graph

def main(folder_name):
    #folder_name = "../../../experiments/"
    b = BuildTree(cosine_similarity, jaccard_dependency, 
                  buildGraph, folder_name)
    return b 

if __name__ == "__main__":
    main()
