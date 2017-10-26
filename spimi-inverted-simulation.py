test_tokens = [
{"term": "apple", "docID": 1},
{"term": "insatiable", "docID": 1},
{"term": "apple", "docID": 2},
{"term": "herring", "docID": 2},
{"term": "incredulous", "docID": 3},
{"term": "insatiable", "docID": 4}
]

def spimi_invert(tokens):
    output_file = {}
    dictionary = {}

    token_index = 0
    memory_used = 0
    max_memory = 35

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

print spimi_invert(test_tokens)
# {'insatiable': [1, 4], 'herring': [2], 'apple': [1, 2], 'incredulous': [3]}
