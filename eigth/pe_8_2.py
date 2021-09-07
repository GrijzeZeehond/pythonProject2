def four_letter_word():
    """
    asks the user for input until the user gives a four letter word. prints ending message and ends program.
    """

    while True:
        word = input('Geef een string van vier letters: ')
        length = len(word)
        if length == 4:
            print('Inlezen van correcte string: {} is geslaagd'.format(word))
            break
        else:
            print('{} heeft {} letters'.format(word, length))

four_letter_word()