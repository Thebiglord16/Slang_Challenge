
def calculateNGrams(text, n):
    n_grams = []
    for i in range(len(text)+1 -n):
        n_grams.append(text[i:i+n])
    return n_grams
    
def mostFrequentNGram(text, n):
    n_grams = {}
    for i in range(len(text)+1 -n):
        n_gram = text[i:i+n]
        if n_gram in n_grams:
            n_grams[n_gram] += 1
        else:
            n_grams[n_gram] = 1
    return max(n_grams, key = n_grams.get)

