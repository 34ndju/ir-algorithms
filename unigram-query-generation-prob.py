def unigram_query_generation_probability_estimation(query, document):
    #naive bayes, assuming p{query) and p(document) are uniform and bag-of-words model
    words = {}
    num_words = 0
    for word in document.split():
        if word not in words:
            words[word] = 0
        words[word] += 1
        num_words += 1

    total_probability = 1
    for query_word in query.split():
        total_probability *= (words[query_word] / float(num_words)) if query_word in words else 0

    return total_probability


def run():
    document = "injustice anywhere is an injustice everywhere the time is always right to do what is right we must build dikes of courage to hold back the flood of fear seeking is not always believing we must use time creatively a lie cannot live a right delayed is a right denied"

    print unigram_query_generation_probability_estimation("injustice is", document)

if __name__ == '__main__':
    run()
    #0.004
    #
