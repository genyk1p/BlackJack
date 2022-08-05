class Dealer:
    cards = []
    cards_sum = 0
    more_2_card = False

    def take_cards(self, card):
        """
        The method takes one random card from the deck for the dealer
        :param card: tuple card for example ('♦', 'Jack', 10)
        :return: list of tuple with cards
        """
        self.cards.append(card)
        return self.cards

    def check_dealer_cards(self):
        """
        This function returns the number of points according to the dealer's cards.
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

    def show_dealer_card(self):
        print('Dealer have:')
        if not self.more_2_card:
            len0 = len(self.cards[0][0] + self.cards[0][1]) + 1
            for index, value in enumerate(self.cards):
                if index == 1:
                    print('*' * len0)
                else:
                    print(value[0] + ' ' + value[1])
        else:
            for index, value in enumerate(self.cards):
                print(value[0] + ' ' + value[1])

    def dealer_def_data(self):
        self.cards = []
        self.cards_sum = 0
        self.more_2_card = False




