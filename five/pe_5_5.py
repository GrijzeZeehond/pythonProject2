def kwadraten_som(grondgetallen):
    """
    Takes a list containing integers as input (grondgetallen). Returns the total sum of all the positive numbers in the
    list after squaring them (n1*n1) + (n2*n2) ... (n-1*n-1)
    """
    total = 0
    for num in grondgetallen:
        if num > 0:
            total += num * num
    return total

print(kwadraten_som([4,3,-5]))