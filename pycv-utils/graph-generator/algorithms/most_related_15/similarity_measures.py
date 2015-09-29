def cosine_similarity(exp1, exp2):
  """ calculate the cosine similarity of 2 experiments """
  words1, vector1 = exp1
  words2, vector2 = exp2

  similarity = 0.0
  for idx1, word in enumerate(words1):
    # if a word is in both exp1 and exp2, similarity increased by tfidf1 * tfidf2
    if word in words2:
      idx2 = words2.index(word)
      similarity += vector1[idx1] * vector2[idx2]
  return similarity

def jaccard_dependency(exp1, exp2):
  """ 
    calculate the direction of dependence of 2 experiments 
    if exp1 is parent of exp2 return 0 
                    otherwise return 1
  """
  words1, _ = exp1
  words2, _ = exp2
  l1 = len(words1)
  l2 = len(words2)
  l_intersect = len(set(words1).intersection(set(words2)))
  return 0 if l_intersect / float(l1) >= l_intersect / float(l2) else 1

