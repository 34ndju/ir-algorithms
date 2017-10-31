def spimi_map(collection):
    # docID is associated with spot in array
    mapped_tokens = []
    for i, doc in enumerate(collection):
        terms = doc.split()
        for term in terms:
            mapped_tokens.append({"term":term, "docID": i})
    return mapped_tokens


def spimi_reduce(tokens):
    output_file = {}
    dictionary = {}

    token_index = 0
    memory_used = 0
    max_memory = 70

    while memory_used < max_memory and token_index < len(tokens):
        token = tokens[token_index]
        if token["term"] not in dictionary:
            dictionary[token["term"]] = []
            postings_list = dictionary[token["term"]]
        else:
            postings_list = dictionary[token["term"]]

        postings_list.append(token["docID"])
        memory_used+=1
        token_index+=1
    return dictionary

def run():
    collection = []
    collection.append("injustice anywhere is an injustice everywhere")
    collection.append("the time is always right to do what is right")
    collection.append("we must build dikes of courage to hold back the flood of fear")
    collection.append("seeking is not always believing")
    collection.append("we must use time creatively")
    collection.append("a lie cannot live")
    collection.append("a right delayed is a right denied")

    mapped_collection = spimi_map(collection)

    print spimi_reduce(mapped_collection)

#run()
'''
{'right': [1, 1, 6, 6], 'is': [0, 1, 1, 3, 6], 'back': [2], 'an': [0],
'fear': [2], 'lie': [5], 'what': [1], 'to': [1, 2], 'flood': [2], 'live': [5],
'believing': [3], 'injustice': [0, 0], 'denied': [6], 'creatively': [4], 'build': [2],
'do': [1], 'we': [2, 4], 'seeking': [3], 'time': [1, 4], 'use': [4], 'delayed': [6],
'courage': [2], 'everywhere': [0], 'not': [3], 'hold': [2], 'must': [2, 4], 'a': [5, 6, 6],
'always': [1, 3], 'dikes': [2], 'anywhere': [0], 'cannot': [5], 'of': [2, 2], 'the': [1, 2]}
'''
