def ngrams(n, string):
    ngrams = set()
    start = 0
    end = start + n
    while end <= len(string):
        ngrams.add(string[start:end])
        start+=1
        end+=1
    return ngrams

#jaccard coefficient for n-grams of two words
def jaccard(n, string1, string2):
    ngram1 = ngrams(n, string1)
    ngram2 = ngrams(n, string2)

    intersection_size = len(ngram1 & ngram2)
    union_size = len(ngram1 | ngram2)

    return intersection_size / float(union_size)

print jaccard(3, "house", "houser")
# 0.75

print jaccard(3, "intersection", "intention")
# 0.307
