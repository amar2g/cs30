import random

class Card:
    # initialize card w/ suit and value
    def __init__(self, value, suit):
        self.VALUE = value  
        self.SUIT = suit   

    def __str__(self):
        value_names = {1: "ace", 11: "jack", 12: "queen", 13: "king"}
        suit_names = {1: "hearts", 2: "diamonds", 3: "clubs", 4: "spades"}
        
        value = value_names.get(self.VALUE, str(self.VALUE))
        suit = suit_names[self.SUIT]
        return f"{value} of {suit}"

    def __repr__(self):
        return f"Card(value={self.VALUE}, suit={self.SUIT})"

class Deck:
    # initialize new deck by creating 52 card combinations
    def __init__(self):
        self.CARDS = []
        self.create_deck()
    
    def create_deck(self):
        for suit in range(1, 5): # iterate through suits
            for value in range(1, 14): # iterate through values
                self.CARDS.append(Card(value, suit))
        return self.CARDS 
    
    def shuffle_deck(self):
        random.shuffle(self.CARDS)

    def draw_top_card(self):
        if len(self.CARDS) > 0: # check if deck has cards
            return self.CARDS.pop(0) # rmv & return 1st card
        return None 
    
    def get_deck_size(self):
        return len(self.CARDS)


class Player:
    def __init__(self, name):
        self.NAME = name # name
        self.CARDS = [] # personal deck
    
    def get_deck_size(self):
        return len(self.CARDS)
    
    def get_card_from_top_of_deck(self):
        if len(self.CARDS) > 0: # check if player has cards
            return self.CARDS.pop(0) # rmv 1st card from list
        return None
    
    def add_card_to_bottom_of_deck(self, card):
        if card is not None: # check if card none before adding
            self.CARDS.append(card) # append to end of list

def main():
    # create two player obj with names
    PLAYER1 = Player("Rosencrantz")
    PLAYER2 = Player("Guidenstern")
    
    # create and shuffle deck
    DECK = Deck()
    DECK.shuffle_deck()
    
    # distribute cards evenly between players
    for i in range(DECK.get_deck_size() // 2): # each player gets 1 card per iteration
        PLAYER1.add_card_to_bottom_of_deck(DECK.draw_top_card())
        PLAYER2.add_card_to_bottom_of_deck(DECK.draw_top_card())
    
    # if odd card left give ot player 1
    if DECK.get_deck_size() > 0:
        PLAYER1.add_card_to_bottom_of_deck(DECK.draw_top_card())
    
    # each player draws 1 card frm the top of their deck
    CARDS = [] # drawn cards
    CARDS.append(PLAYER1.get_card_from_top_of_deck()) # player 1 draws
    CARDS.append(PLAYER2.get_card_from_top_of_deck()) # player 2 draws
    
    # print the values of drawn cards
    print(CARDS[0], CARDS[1])
# run everythign
if __name__ == "__main__":
    main()
