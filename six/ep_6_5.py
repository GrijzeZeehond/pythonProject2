

def gemiddelde():
    """
    asks the user to give a random sentence and will return the average word length of the sentence.
    """
    sentence = input("geef een willekeurige zin: ")

    list_words = sentence.split(sep=' ')
    total = 0
    for word in list_words:
        total += len(word)
    return total / len(list_words)

    print(list_words)

print(gemiddelde())