def mean(list):
    """
    Takes a list of numbers as input and returns the mean average of them.
    """
    total = 0

    for item in list:
        total += item

    return total / len(list)

def analyzer(string_of_ints):
    """
    Takes a string composed of integers divided by dashes '1-3-5-76-4-20-3'. splits the paramter into a list with
    numbers. Sorts the list from small to big. returns as a tuple the sorted list; the biggest value; the smallest
    value; the number of values; the total sum of values; the mean.
    """

    string_list = string_of_ints.split(sep='-')
    numbers = []

    for num in string_list:
        numbers.append(int(num))
    numbers.sort()

    maximum = numbers[-1]
    minimum = numbers[0]


    return (numbers, maximum, minimum, len(numbers), sum(numbers), mean(numbers))

string = "5-9-7-1-7-8-3-2-4-8-7-9"
output_string = 'Gesorteerde lijst van ints: {}\n' \
    'Grootste getal: {} en Kleinste getal: {}\n' \
    'Aantal getallen: {} en Som van de getallen: {}\n' \
    'Gemiddelde: {}'

sorted_list, maximum, minimum, length_list, sum_numbers, mean_numbers = analyzer(string)

print(output_string.format(sorted_list, maximum, minimum, length_list, sum_numbers, mean_numbers))