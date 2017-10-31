from spimi_map_reduce import spimi_map, spimi_reduce
import math

def get_idf(term, inverted_index, collection_size):
    log_base = 2
    seen = set()
    for doc in inverted_index[term]:
        seen.add(doc)
    return math.log(float(collection_size) / len(seen), log_base)

def get_tf(term, inverted_index, docID):
    freq = 0
    for doc in inverted_index[term]:
        if doc == docID:
            freq += 1
    return freq

def ranked_retrieval(terms, collection):
    mapped_collection = spimi_map(collection)
    inverted_index = spimi_reduce(mapped_collection)

    scores = []
    for i in range(len(collection)):
        # first index is docID, second index is score based on term
        scores += [[i, 0]]

    for term in terms:
        for docID, document in enumerate(collection):
            scores[docID][1] += get_tf(term, inverted_index, docID) * get_idf(term, inverted_index, len(collection))

    sorted_scores = sorted(scores, key=lambda k: k[1], reverse=True)
    for sorted_score in sorted_scores:
        print "docID: {0}, Text: {1}".format(sorted_score[0], collection[sorted_score[0]])

def run():
    collection = []
    collection.append("injustice anywhere is an injustice everywhere")
    collection.append("the time is always right to do what is right")
    collection.append("we must build dikes of courage to hold back the flood of fear")
    collection.append("seeking is not always believing")
    collection.append("we must use time creatively")
    collection.append("a lie cannot live")
    collection.append("a right delayed is a right denied")
    collection.append("if this is a holder for is and it is long then it really is made of is")

    ranked_retrieval(["is", "right"], collection)

run()
'''
docID: 1, Text: the time is always right to do what is right
docID: 6, Text: a right delayed is a right denied
docID: 7, Text: if this is a holder for is and it is long then it really is made of is
docID: 0, Text: injustice anywhere is an injustice everywhere
docID: 3, Text: seeking is not always believing
docID: 2, Text: we must build dikes of courage to hold back the flood of fear
docID: 4, Text: we must use time creatively
docID: 5, Text: a lie cannot live
'''
