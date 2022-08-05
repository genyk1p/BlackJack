class Player:
    balance = 10
    cards_sum = 0
    cards = []

    def increase_balance(self, value):
        self.balance += value
        return self.balance

    def decrease_balance(self, value):
        self.balance -= value
        return self.balance

    def take_cards(self, card):
        """
        The method takes one random card from the deck for the player
        :param card: tuple card for example ('♦', 'Jack', 10)
        :return: list of tuple with cards
        """
        self.cards.append(card)
        return self.cards

    def check_player_cards(self):
        """
        This function returns the number of points according to the player's cards.
        """
        for card in self.cards:
            self.cards_sum += card[2]
        if self.cards_sum <= 21:
            return self.cards_sum
        else:
            self.cards_sum = 0
            for suit, card_name, card_value in self.cards:
                if card_name == 'Ace':
                    card_value = 1
                self.cards_sum += card_value
            return self.cards_sum

    def show_player_cards(self):
        print('Player have:')
        if self.cards_sum > 21:
            print('You lost')
        if self.cards_sum <= 21:
            for card in self.cards:
                print(card[0] + ' ' + card[1])

    def player_def_data(self):
        self.cards = []
        self.cards_sum = 0
