def ask_bid(balance):
    """
    The function asks the player what he wants to bet
    param balance: int current player balance
    :return: int player bid
    """
    while True:
        try:
            int_number = int(input('Please place a bid '))
        except:
            print('The entered value is not a number, please try again')
            continue
        else:
            if int_number <= balance:
                return int_number
            else:
                print(f"Unfortunately your chip balance is {balance}, it is too low to place this bet, please place "
                      f"another bet.")


def ask_1_2(question=''):
    """
    The function returns the numbers 1 or 2
    :param question: str The text that we display to the player when we ask for a number
    :return: int 1 or 2
    """
    while True:
        try:
            int_number = int(input(question))
        except:
            print('The entered value is not a number, please try again')
            continue
        else:
            if int_number in [1, 2]:
                return int_number
