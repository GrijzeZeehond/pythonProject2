students = {'Donna': 8, 'Fritzy': 9.5, 'Betty':9.2, 'Donny': 8.9, "Dallis":6}

def hoogvliegers(dict_studenten_cijfers):
    """
    Takes a dict as input. The dict consists of student names(keys) and grades(values). Returns a new dictionary
    containing only the students with a grade of 9.0 and above.
    """
    summa_cum_laude_students = {}
    for key, value in dict_studenten_cijfers.items():
        if value >= 9.0:
            summa_cum_laude_students[key] = value
    return summa_cum_laude_students

print(hoogvliegers(students))
