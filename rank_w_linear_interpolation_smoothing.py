import urllib2
from bs4 import BeautifulSoup

def rank_by_linear_interpolation(query, collection, lambda_weight):
    collective_term_map = {}
    collective_num_terms = 0

    collection_term_maps = {}

    for name, document_text in collection.iteritems():
        curr_doc_term_map = {}
        curr_doc_term_map["NUM_TERMS"] = 0

        for term in document_text.split():
            if term not in collective_term_map:
                collective_term_map[term] = 0
            collective_term_map[term] += 1
            collective_num_terms += 1

            if term not in curr_doc_term_map:
                curr_doc_term_map[term] = 0
            curr_doc_term_map[term] += 1
            curr_doc_term_map["NUM_TERMS"] += 1

        collection_term_maps[name] = curr_doc_term_map

    query_probabilities_per_doc = {}
    for name, term_map in collection_term_maps.iteritems():
        probability = 1
        for query_term in query.lower().split():
            term_probability = 0
            term_probability += lambda_weight * ( (term_map[query_term] / float(term_map["NUM_TERMS"])) if query_term in term_map else 0)
            term_probability += (1 - lambda_weight) * ( (collective_term_map[query_term] / float(collective_num_terms)) if query_term in collective_term_map else 0)
            probability *= term_probability
        query_probabilities_per_doc[name] =  probability

    descending_query_probabilities = sorted(query_probabilities_per_doc, key=query_probabilities_per_doc.get, reverse=True)

    return descending_query_probabilities


def run_with_query(query):
    lambda_weight = 0.8

    collection_links = {}
    collection_links["Donald Glover"] = "https://en.wikipedia.org/wiki/Donald_Glover"
    collection_links["Kanye West"] = "https://en.wikipedia.org/wiki/Kanye_West"
    collection_links["J Cole"] = "https://en.wikipedia.org/wiki/J._Cole"
    collection_links["Eminem"] = "https://en.wikipedia.org/wiki/Eminem"
    collection_links["J.K. Rowling"] = "https://en.wikipedia.org/wiki/J._K._Rowling"
    collection_links["Peter Thiel"] = "https://en.wikipedia.org/wiki/Peter_Thiel"
    collection_links["Max Levchin"] = "https://en.wikipedia.org/wiki/Max_Levchin"
    collection_links["Jiawei Han"] = "https://en.wikipedia.org/wiki/Jiawei_Han"
    collection_links["Jen-Hsun Huang"] = "https://en.wikipedia.org/wiki/Jensen_Huang"

    collection = {}

    for name, link in collection_links.iteritems():
        connection = urllib2.urlopen(link)
        html = connection.read()
        connection.close()
        soup = BeautifulSoup(html, 'html5lib')

        collection[name] = soup.find("div", {"id":'bodyContent'}).text.lower()

    print rank_by_linear_interpolation(query, collection, lambda_weight)


if __name__ == '__main__':
    #run_with_query("venture capitalist and internet entrepreneur")
    # ['Peter Thiel', 'Max Levchin', 'Jen-Hsun Huang', 'Donald Glover', 'Kanye West', 'Eminem', 'J Cole', 'J.K. Rowling', 'Jiawei Han']

    #run_with_query("controversy")
    # ['Kanye West', 'Peter Thiel', 'Eminem', 'J Cole', 'Max Levchin', 'Jen-Hsun Huang', 'J.K. Rowling', 'Donald Glover', 'Jiawei Han']

    #run_with_query("research")
    # ['Jiawei Han', 'Peter Thiel', 'J.K. Rowling', 'J Cole', 'Max Levchin', 'Eminem', 'Jen-Hsun Huang', 'Donald Glover', 'Kanye West']


    run_with_query("Grammys")
