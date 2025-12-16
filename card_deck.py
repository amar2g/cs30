import random

class Card:
    # initialize card w/ suit and value
    # suit (str) = single char represent the suit h, s, d, c
    # value (int) = num val of card 1-13
    def __init__(self, suit, value): 
        self.suit = suit
        self.value = value
    
    def get_english_name(self):
        value_names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"} # value to english 
        
        if self.value in value_names: # check for special card
            value_str = value_names[self.value] 
        else: # regular card
            value_str = str(self.value) 

        suit_names = {"H": "Hearts", "S": "Spades","D": "Diamonds", "C": "Clubs"} # suit to english
        
        suit_str = suit_names.get(self.suit, self.suit) # handle unexpected values
        
        return f"{value_str} of {suit_str}"

class Deck:
    # initialize new deck by creating 52 card combinations
    def __init__(self):
        self.cards = [] # store Card objects
        suits = ["H", "S", "D", "C"]  
        values = list(range(1, 14)) # 1-13
        
        for suit in suits: # iterate through suit and value
            for value in values:
                card = Card(suit, value) # create 1 Card object of every combination
                self.cards.append(card) # fill list
    
    # randomly shuffle deck
    def shuffle(self):
        random.shuffle(self.cards)
    
    # draw top card from deck
    def draw(self):
        if self.size() > 0:
            return self.cards.pop() # rmv last card
        else:
            return None
    
    # calc num of cards in deck
    def size(self):
        return len(self.cards)

if __name__ == "__main__":
    # create 2 decks
    deck_1 = Deck()
    deck_2 = Deck()
    
    # print inital size = 52
    print(f"deck 1 size: {deck_1.size()}")
    print(f"deck 2 size: {deck_2.size()}")
    
    # shuffle decks
    deck_1.shuffle()
    deck_2.shuffle()
    
    # draw 1 card from each deck
    card_1 = deck_1.draw()
    card_2 = deck_2.draw()
    
    # print name of card
    if card_1:
        print(f"deck 1: {card_1.get_english_name()}")
    else:
        print("deck 1's empty")
    
    if card_2:
        print(f"deck 2: {card_2.get_english_name()}")
    else:
        print("deck 2's empty")
    
    # remaining crads
    print(f"remaining cards in deck 1: {deck_1.size()}")
    print(f"remaining cards in deck 2: {deck_2.size()}")
