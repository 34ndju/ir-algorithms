from ranked_retrieval_tf_idf import get_tf

def get_champions_set_for_term(term, r, collection):
    champions_set = set()
    list_of_tf = []
    for i, doc in enumerate(collection):
        list_of_tf.append([i, get_tf(term, doc)])

    champions_set = set()
    for tf in sorted(list_of_tf, key = lambda k:k[1], reverse=True)[:r]:
        champions_set.add(tf[0])

    return champions_set


#print and_of_tuple_list([1],[1,2])

def get_champions_list(terms, k, r, collection):
    complete_champion_set = get_champions_set_for_term(terms[0], r, collection)
    complete_champion_list = []
    for term in terms[1:]:
        complete_champion_set &= get_champions_set_for_term(term, r, collection)

    k_champions_list = sorted(list(complete_champion_set), reverse=True)[:k]

    return k_champions_list[:k]


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

    #should be non-stop words, but collection is too small for this purpose
    print get_champions_list(["is", "a"], 4, 5, collection)

run()
# [7, 6, 1, 0]
