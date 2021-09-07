card_file = 'pe_6_2_kaartnummers'
def read_lines(file):
    """
    reads the document. Places each line as an element in a list.
    """
    with open(file) as file:
        lines_list = file.readlines()
    return lines_list

def biggest_card(file):
    """
    takes a file with cardnumbers as input. Returns how many lines the file contains, what the biggest cardnumber is and
    on which line in the file the biggest cardnumber is located.
    """

    lines_list = read_lines(card_file)

    final_string_format = 'Deze file telt {} regels\nHet grootste kaartnummer is: {} en dat staat op regel {}'

    #calcutates following values
    lines_amount = len(lines_list)
    highest_cardnumber = max(lines_list)
    line_highest_cardnumber = 1
    for line in lines_list:
        if line == highest_cardnumber:
            break
        else:
            line_highest_cardnumber += 1

    return final_string_format.format(lines_amount, highest_cardnumber[:6], line_highest_cardnumber)

print(biggest_card(card_file))