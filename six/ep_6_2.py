card_file = 'pe_6_2_kaartnummers'
def read_lines(file):
    """
    reads the document. Places each line as an element in a list.
    """
    with open(file) as file:
        lines_list = file.readlines()
    return lines_list


def pretty_print(card_file):
    """
    takes the name of a file with people and their associated cards (card_file) as input and returns a string with all
    the people and the card in their posession in a nice readable format.
    """
#
    return_string = ''

    lines_list = read_lines(card_file)

    #for each element of the list, splits the element at the comma and assigns the cardvalue and name respectively.
    for line in lines_list:
        card_number, name = line.split(sep=',')
        return_string += '{} heeft kaartnummer: {}\n'.format(name[:-2], card_number)
    return return_string

print(pretty_print(card_file))