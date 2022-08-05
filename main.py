from cards import Cards
from dealer_account import Dealer
from functions import ask_bid, ask_1_2
from player_account import Player

# Create instances of the player and dealer class
player = Player()
dealer = Dealer()

print('Welcome to the game of blackjack!')
while True:
    # We set the variables to the default value at the start of a new round
    end_round_marker = 0
    player.player_def_data()
    dealer.dealer_def_data()
    pass_marker = 0
    cards = Cards()

    print('\n' * 100)
    print(f'Your balance is {player.balance}')
    bid = ask_bid(player.balance)
    # Handing out cards
    for i in range(2):
        dealer.take_cards(cards.take_random_card())
        player.take_cards(cards.take_random_card())

    dealer.show_dealer_card()
    player.show_player_cards()

    # The player draws cards if necessary
    while pass_marker == 0:
        hit = ask_1_2('Hit more - 1, pass - 2 ')
        if hit == 1:
            player.take_cards(cards.take_random_card())
            print('\n' * 100)
            dealer.show_dealer_card()
            player.show_player_cards()
            if player.check_player_cards() > 21:
                player.decrease_balance(bid)
                end_round_marker = 1
                pass_marker = 1
                print('Dealer - win')
        elif hit == 2:
            player.check_player_cards()
            pass_marker = 1
    # Winner Check
    if end_round_marker == 0:
        dealer.more_2_card = True
        while True:
            dealer.take_cards(cards.take_random_card())
            if dealer.check_dealer_cards() >= 17:
                break
        print('\n' * 100)
        dealer.show_dealer_card()
        player.show_player_cards()
        if dealer.check_dealer_cards() > 21:
            player.increase_balance(bid)
            print('Player - win')
        elif dealer.cards_sum == player.cards_sum:
            print('Draw')
        elif dealer.cards_sum > player.cards_sum:
            player.decrease_balance(bid)
            print('Dealer - win')
        elif dealer.cards_sum < player.cards_sum:
            player.increase_balance(bid)
            print('Player - win')
    if player.balance <= 0:
        print(f'Game over your balance is {player.balance}')
        break
    # We ask the player if he wants to play another game.
    new_game = ask_1_2('If you want to play once more press 1, if you want to end game press 2 ')
    if new_game == 1:
        new_game = 0
    elif new_game == 2:
        print(f'Game over your balance is {player.balance}')
        break
