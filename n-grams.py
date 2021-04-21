#The implementation of calculateNGrams has O(m-n) as it runs some m-n+1 times the constant O(n) 
# python slice operation (where m is the lenght of the text and n is the lenght of the n-grams)
def calculateNGrams(text, n):
    n_grams = [] # answer variable
    for i in range(len(text)+1 -n): # according to the definition of an n-gram it will have m+1-n total strings,
                                    # so this accounts for the number of iterations required to fin the n-grams
        n_grams.append(text[i:i+n]) # finds every adjacent n-gram slicing the text
    return n_grams                  # returns

#The implementation of mostFrequentNGrams has O(m-n) time as it runs some m-n+1 times the constant O(n) 
# python slice operation and the constant O(1) dict find 
# operation as python dictionarys behave as hashmaps and have constant lookup time
# finding the max value is out of the loop and it takes linear time equal
# (where m is the lenght of the text and n is the lenght of the n-grams)    
def mostFrequentNGram(text, n):
    n_grams = {} # Python dictionary used for the answer as lookup times are faster in this data structure
    for i in range(len(text)+1 -n): # according to the definition of an n-gram it will have m+1-n total strings,
                                    # so this accounts for the number of iterations required to fin the n-grams
        n_gram = text[i:i+n]        # finds every adjacent n-gram slicing the text
        if n_gram in n_grams:       # looks if the n_gram already exists and if it does adds one to the count
            n_grams[n_gram] += 1    
        else:                       # if the n_gram does not exist adds it to the dictionary
            n_grams[n_gram] = 1
    return max(n_grams, key = n_grams.get) # finds the key of the max value in the dictionary and returns it

