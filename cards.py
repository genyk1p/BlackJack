from random import randint


# Cards list
class Cards:
    cards = [('♦', '2', 2), ('♦', '3', 3), ('♦', '4', 4), ('♦', '5', 5), ('♦', '6', 6), ('♦', '7', 7), ('♦', '8', 8),
             ('♦', '9', 9), ('♦', '10', 10), ('♦', 'Jack', 10), ('♦', 'Queen', 10), ('♦', 'King', 10),
             ('♦', 'Ace', 11), ('♥', '2', 2), ('♥', '3', 3), ('♥', '4', 4), ('♥', '5', 5), ('♥', '6', 6),
             ('♥', '7', 7), ('♥', '8', 8), ('♥', '9', 9), ('♥', '10', 10), ('♥', 'Jack', 10), ('♥', 'Queen', 10),
             ('♥', 'King', 10), ('♥', 'Ace', 11), ('♣', '2', 2), ('♣', '3', 3), ('♣', '4', 4), ('♣', '5', 5),
             ('♣', '6', 6), ('♣', '7', 7), ('♣', '8', 8), ('♣', '9', 9), ('♣', '10', 10), ('♣', 'Jack', 10),
             ('♣', 'Queen', 10), ('♣', 'King', 10), ('♣', 'Ace', 11), ('♠', '2', 2), ('♠', '3', 3), ('♠', '4', 4),
             ('♠', '5', 5), ('♠', '6', 6), ('♠', '7', 7), ('♠', '8', 8), ('♠', '9', 9), ('♠', '10', 10),
             ('♠', 'Jack', 10), ('♠', 'Queen', 10), ('♠', 'King', 10), ('♠', 'Ace', 11)]

    def take_random_card(self):
        """
        Еhe method takes one random card from the list and removes it from the list
        :return: tuple with card
        """
        return self.cards.pop(randint(0, len(self.cards) - 1))
