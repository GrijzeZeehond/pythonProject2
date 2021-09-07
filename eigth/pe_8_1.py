def total_sum():
    """
    Keeps asking for input until the user puts in the number 0.
    prints the number of guesses and the total sum of all the guessed values.
    """
    active = True
    rounds = 0
    total = 0

    while active:
        n = input('Geef een getal: ')
        if n == '0':
            active = False
        else:
            rounds += 1
            total += int(n)
    print('Er zijn {} getallen ingevoerd, de som is: {}'.format(rounds, total))

total_sum()
