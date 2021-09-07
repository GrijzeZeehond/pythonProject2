import time

bike_file = 'pe_6_4_hardlopers'
def add_runner(file):
    """
    takes the location of a document as input. makes or opens the document. Asks the user for input. gets the time. Adds
     the input withg the time to the end of the document and closes it.
    """
    active = True
    while active:
        with open(bike_file, 'a') as open_file:
            name = input('Enter runner\'s name (press enter to leave): ')
            if not name:
                active = False
            else:
                local_time = time.localtime()
                current_time = time.strftime('%b/%d/%m/%Y, %H:%M:%S, ', local_time)
                open_file.write(current_time + name + '\n')

add_runner(bike_file)
