
def calculateNGrams(text, n):
    n_grams = []
    print(len(text)+1 -n)
    for i in range(len(text)+1 -n):
        n_grams.append(text[i:i+n])
    return n_grams

print(calculateNGrams("to be or not to be", 2))