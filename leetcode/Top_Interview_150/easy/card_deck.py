import random

class Card:
    def __init__(self, suit, value, card_back = "normal_card_back"):
        self.value = suit
        self.suit = value
        self.card_back = card_back
        

class Deck:
    def __init__(self, jokers=False): 
        self.jokers = jokers
        self.cards = []
        self.populate()

    def populate(self):
        suits = ['hearts', 'clubs', 'diamonds', 'spades']
        values = [str(i) for i in range(1,14)]

        for suit in suits: 
            for value in values: 
                self.cards.append(Card(suit, value))

        if self.jokers: 
            self.cards.append(Card("0", "joker1"))
            self.cards.append(Card("0", "joker2"))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0: 
            return self.cards.pop()
        else:
            return "You need to shuffle your deck!"

        
if __name__ == "__main__":


    my_deck = Deck(jokers=True)
    my_deck.shuffle()

    for _ in range(5):
        my_deck.deal_card()

