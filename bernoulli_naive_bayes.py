import math

def extract_classes(docs):
    classes = set()
    for doc in docs:
        classes.add(doc["class"])
    return classes

def extract_vocab(docs):
    vocab = set()
    for doc in docs:
        for word in doc["text"].split():
            vocab.add(word)
    return vocab

def get_num_docs(docs):
    return len(docs)

def get_num_docs_in_class(docs, class_name):
    count = 0
    for doc in docs:
        if doc["class"] == class_name:
            count += 1
    return count

def count_docs_in_class_containing_term(docs, class_name, term):
    count = 0
    for doc in docs:
        if doc["class"] == class_name and doc["text"].find(term) > -1:
            count += 1
    return count

def extract_vocab_from_doc(doc):
    vocab = set()
    for word in doc.split():
        vocab.add(word)
    return vocab

def train_bernoulli_naive_bayes(classes, training_set):
    vocab = extract_vocab(training_set)
    num_docs = get_num_docs(training_set)
    num_docs_per_class = {}
    priors = {}
    cond_prob = {}
    for class_name in classes:
        num_docs_per_class[class_name] = get_num_docs_in_class(training_set, class_name)
        priors[class_name] = float(num_docs_per_class[class_name]) / get_num_docs(training_set)
        for word in list(vocab):
            docs_in_class_containing_term = count_docs_in_class_containing_term(training_set, class_name, word)
            docs_in_class = num_docs_per_class[class_name]
            if word not in cond_prob:
                cond_prob[word] = {}
            cond_prob[word][class_name] = float(docs_in_class_containing_term + 1) / (docs_in_class + 2)
    return vocab, priors, cond_prob

def apply_bernoulli_naive_bayes(classes, tbnb_parameters, doc):
    vocab = tbnb_parameters[0]
    priors = tbnb_parameters[1]
    cond_prob = tbnb_parameters[2]

    vocab_in_doc = extract_vocab_from_doc(doc)
    scores = {}
    for class_name in classes:
        scores[class_name] = math.log(priors[class_name])
        for term in vocab:
            if term in vocab_in_doc:
                scores[class_name] += math.log(cond_prob[term][class_name])
                scores[class_name] -= math.log(1 - cond_prob[term][class_name])

    max_score = 0
    best_class = ""
    for class_name, score in scores.iteritems():
        if score > max_score:
            max_score = score
            best_class = class_name
    return best_class

def run():
    training_set = []
    training_set.append(  { "docID": 1, "text": "Chinese Beijing Chinese", "class": "china"  }  )
    training_set.append(  { "docID": 2, "text": "Chinese Chinese Shanghai", "class": "china"  }  )
    training_set.append(  { "docID": 3, "text": "Chinese Macao", "class": "china"  }  )
    training_set.append(  { "docID": 4, "text": "Tokyo Japan Chinese", "class": "japan"  }  )

    test_set = []
    test_set.append( { "docID": 5, "text": "Chinese Chinese Chinese Tokyo Japan" } )

    test_doc = { "docID": 5, "text": "Chinese Chinese Chinese Tokyo Japan" }["text"]

    classes = extract_classes(training_set)

    print apply_bernoulli_naive_bayes(classes, train_bernoulli_naive_bayes(classes, training_set), test_doc)

if __name__ == '__main__':
    run()
