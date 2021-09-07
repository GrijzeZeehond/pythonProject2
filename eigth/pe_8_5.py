def namen():
    """
    Asks the user for names from students. Keeps track of how often each name has been mentioned. Returns these valeus
    in a dict.
    """
    active = True
    counters = {}
    while active:
        student = input('Volgende naam: ')

        if student == '':
            active = False
        elif student in counters:
            counters[student] += 1
        else:
            counters[student] = 1

    return counters

if __name__ == '__main__':
    print(namen())