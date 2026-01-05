import random

class Card:
    # initialize card w/ suit and value
    def __init__(self, suit, value): # suit (str) = single char represent the suit h, s, d, c # value (int) = num val of card 1-13
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

class Player:
    # represent a player w/ a name and cards
    def __init__(self, name): # name (str), initialize empty card list
        self.NAME = name
        self.CARDS = []   
    
    def getDeckSize(self): # num of cards in deck
        return len(self.CARDS)
    
    def getCardFrmTopDeck(self): #rmv top card from deck
        if self.getDeckSize() > 0:
            return self.CARDS.pop(0)
        return None 
    
    def addCardBtmDeck(self, card): #add card to bottom of deck
        if card is not None: 
            self.CARDS.append(card)  

#create 2 players w/ names above
PLAYER1 = Player("Rosencrantz")
PLAYER2 = Player("Guidenstern")

# create deck and shuffle it
DECK = Deck()
DECK.shuffle()

# split cards b/t both players
for i in range(DECK.size() // 2):  
    PLAYER1.addCardBtmDeck(DECK.draw())
    PLAYER2.addCardBtmDeck(DECK.draw())

# give odd card left to player 1
if DECK.size() > 0:  
    PLAYER1.addCardBtmDeck(DECK.draw())

# each player draw top card for comparisson
CARDS = []
CARDS.append(PLAYER1.getCardFrmTopDeck())
CARDS.append(PLAYER2.getCardFrmTopDeck())

# print values of cards
print(CARDS[0].value, CARDS[1].value)
