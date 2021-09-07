import random
def simulate_dice():
    """
    simulates a six sided dice being thrown. returns the result as int.
    """
    throw = random.randint(1, 6)
    return throw

def monopolyworp():
    """
    throws two dice. If both stones have the same value's, throw again. After throwing three times the player is sent to
    prison.
    """
    counter = 0
    throws = []

    while counter < 3:
        counter += 1
        dice1 = simulate_dice()
        dice2 = simulate_dice()
        throws.append((dice1, dice2))

        for throw1, throw2 in throws:
            print('{} + {} = {}'.format(throw1, throw2, throw1 + throw2))
        print(throws)

        if dice1 != dice2:
            counter = 4

    if counter == 3:
        print('direct naar de gevangenis')


if __name__ == '__main__':
    monopolyworp()
