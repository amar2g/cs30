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
            return self.CARDS.pop(-1) # rmv & return 1st card
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
            return self.CARDS.pop(-1) # rmv 1st card from list
        return None
    
    def add_card_to_bottom_of_deck(self, card):
        if card is not None: # check if card none before adding
            self.CARDS.append(card) # append to end of list

class Game:
    def __init__(self):
        self.PLAYER1 = Player("bill")
        self.PLAYER2 = Player("donald")

        print(f"players created: {self.PLAYER1.NAME} and {self.PLAYER2.NAME}")
        
        self.DECK = Deck()
        
        # game vars
        self.ROUND_NUMBER = 0
        self.IN_PLAY = []
        self.ROUND_WINNER = 0
        
        self.DECK.shuffle_deck()
        
        self.deal_deck_to_players()
    
    def create_players(self):
        # created in __init__
        pass
    
    def deal_deck_to_players(self):
        while self.DECK.get_deck_size() > 0: # deal until deck empty
            card1 = self.DECK.draw_top_card() 
            card2 = self.DECK.draw_top_card()
            # add cards to player decks
            if card1:
                self.PLAYER1.add_card_to_bottom_of_deck(card1)
            if card2:
                self.PLAYER2.add_card_to_bottom_of_deck(card2)
    
    def move_cards_to_winner(self, player):
        for card in self.IN_PLAY: # append cards to winner deck
            if card:
                player.add_card_to_bottom_of_deck(card)

        # clear in play cards
        self.IN_PLAY = []
    
    def run(self):
        # continue play until round 1000
        while (self.PLAYER1.get_deck_size() > 0 and 
               self.PLAYER2.get_deck_size() > 0 and 
               self.ROUND_NUMBER < 100):
            
            self.ROUND_NUMBER += 1
            
            # player draws card
            card1 = self.PLAYER1.get_card_from_top_of_deck()
            card2 = self.PLAYER2.get_card_from_top_of_deck()
            
            # append cards to in play list
            self.IN_PLAY.append(card1)
            self.IN_PLAY.append(card2)
            
            # val of ace to 14
            value1 = card1.VALUE if card1.VALUE != 1 else 14
            value2 = card2.VALUE if card2.VALUE != 1 else 14

            print(f"round: {self.ROUND_NUMBER}; {self.PLAYER1.NAME}: {card1}, {self.PLAYER2.NAME} {card2}")
            
            if value1 > value2: # calc the winner
                self.ROUND_WINNER = 1
                self.move_cards_to_winner(self.PLAYER1)
                print(f"{self.PLAYER1.NAME} won")
            elif value2 > value1:
                self.ROUND_WINNER = 2
                self.move_cards_to_winner(self.PLAYER2)
                print(f"{self.PLAYER2.NAME} won")
            else:
                self.ROUND_WINNER = random.choice([1, 2]) # if tie then coin flip
                winner = self.PLAYER1 if self.ROUND_WINNER == 1 else self.PLAYER2
                print(f"tie, {winner.NAME} won by coin flip")
                self.move_cards_to_winner(winner)

        print(f"\nrounds played: {self.ROUND_NUMBER}")

if __name__ == "__main__":
    GAME = Game()
    GAME.run()
