def seizoen(maand):
    """
    Takes an int representing a month and returns the season assosiated with the month.
    """
    if 1 > maand or maand >= 13:
        return 'ongeldig'
    elif 2 < maand <= 5 :
        return 'lente'
    elif 5 < maand <= 8:
        return 'zomer'
    elif 9 < maand <= 11:
        return 'herfst'
    else:
        return 'winter'

print(seizoen(-1))
print(seizoen(13))
print(seizoen(2))
print(seizoen(3))
print(seizoen(5))
print(seizoen(6))
print(seizoen(8))
print(seizoen(9))
print(seizoen(11))
print(seizoen(12))