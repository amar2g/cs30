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
    
    def shuffle_deck(self):
        random.shuffle(self.CARDS)
    
    def draw_card(self):
        if len(self.CARDS) > 0: # check if deck has cards
            return self.CARDS.pop(0) # rmv & return 1st card
        return None
    
    def get_deck_size(self):
        return len(self.CARDS)

class Player:
    def __init__(self, name):
        self.NAME = name
        self.CARDS = []
        self.STAND = False     
        self.HAND = []          
        self.HAND_VALUE = 0     
        self.WINS = 0          

    def get_deck_size(self):
        return len(self.CARDS)
    
    def get_card_from_top_of_deck(self):
        if len(self.CARDS) > 0: # check if player has cards
            return self.CARDS.pop(0) # rmv 1st card from list
        return None
    
    def add_card_to_bottom_of_deck(self, card):
        if card is not None: # check if card none before adding
            self.CARDS.append(card) # append to end of list
    
    def take_card(self, card):
        self.HAND.append(card) # append card to player hand
    
    def set_hand_value(self, value):
        self.HAND_VALUE = value
    
    def stand_hand(self):
        self.STAND = True # signal ending turn
    
    def reset_hand(self):
        self.STAND = False
        self.HAND = []
        self.HAND_VALUE = 0
    
    def add_win(self):
        self.WINS += 1

class Game:
    def __init__(self):
        self.DEALER = Player("dealer")
        self.PLAYER = None
        self.DECK = Deck()
    
    def setup(self):
        player_name = input("enter your name: ") # get name input
        self.PLAYER = Player(player_name)
        self.DECK.shuffle_deck()

    def calc_score(self, hand):
        # j, q, k = 10; ace = 1
        score = 0
        for card in hand:
            if card.VALUE >= 11:  # j, q, k
                score += 10
            else:  # other cards including ace = 1
                score += card.VALUE
        return score
    
    def run(self):
        if self.PLAYER is None:
            print("erorr")
            return
        
        while self.PLAYER.WINS < 3 and self.DEALER.WINS < 3: # play until someone get 3 wins
            self.PLAYER.reset_hand()
            self.DEALER.reset_hand()
            
            print(f"\nround: {self.PLAYER.WINS + self.DEALER.WINS + 1}")
            print(f"score: {self.PLAYER.NAME}: {self.PLAYER.WINS} -- dealer: {self.DEALER.WINS}")
            
            for _ in range(2): # deal 2 cards initially
                self.PLAYER.take_card(self.DECK.draw_card())
                self.DEALER.take_card(self.DECK.draw_card())
        
            player_score = self.calc_score(self.PLAYER.HAND)
            dealer_score = self.calc_score(self.DEALER.HAND)
            
            self.PLAYER.set_hand_value(player_score)
            self.DEALER.set_hand_value(dealer_score)
            
            print(f"\ndealer shows: {self.DEALER.HAND[0].VALUE} and [hidden]")
            print(f"player hand: {self.PLAYER.HAND[0].VALUE}, {self.PLAYER.HAND[1].VALUE} (Total: {player_score})")

            # player's turn
            print(f"\n{self.PLAYER.NAME}'s turn:")

            while not self.PLAYER.STAND and player_score <= 21:
                action = input("hit or stand? (h/s): ").lower()

                if action == 'h': # player hits
                    new_card = self.DECK.draw_card()
                    self.PLAYER.take_card(new_card)
                    player_score = self.calc_score(self.PLAYER.HAND)
                    self.PLAYER.set_hand_value(player_score)
                    
                    print(f"player draws: {new_card.VALUE}; total: {player_score}")
                    
                    if player_score > 21:
                        self.PLAYER.stand_hand()

                elif action == 's': # player stands
                    self.PLAYER.stand_hand()
                    print(f"\nplayer stands with: {player_score}")

                else:
                    print("invalid input")
            
            # Dealer's turn, if player didn't bust
            if player_score <= 21:
                print(f"\ndealer's hand: {self.DEALER.HAND[0].VALUE}, {self.DEALER.HAND[1].VALUE} (Total: {dealer_score})")
                
                while not self.DEALER.STAND:

                    if dealer_score <= 15: # dealer must hit
                        new_card = self.DECK.draw_card()
                        self.DEALER.take_card(new_card)
                        dealer_score = self.calc_score(self.DEALER.HAND)
                        self.DEALER.set_hand_value(dealer_score)
                        
                        print(f"dealer hits, draws: {new_card.VALUE}. Total: {dealer_score}")
                        
                        if dealer_score > 21:
                            print("dealer busted")
                            self.DEALER.stand_hand()
                    else: # dealer must stand <16
                        self.DEALER.stand_hand()
                        print(f"dealer stands with: {dealer_score}")
            
            # winner
            print(f"{self.PLAYER.NAME}: {player_score}")
            print(f"dealer: {dealer_score}")
            
            if player_score > 21: # player busted, dealer wins
                print("player busted, dealer wins")
                self.DEALER.add_win()

            elif dealer_score > 21:
                print(f"{self.PLAYER.NAME} wins, dealer busted")
                self.PLAYER.add_win()

            elif player_score > dealer_score:
                print(f"{self.PLAYER.NAME} wins with higher score")
                self.PLAYER.add_win()

            else:
                print("dealer wins")
                self.DEALER.add_win()
            
            # gather cards back into deck, create new deck when empty
            if self.DECK.get_deck_size() < 10:
                self.DECK = Deck()
                self.DECK.shuffle_deck()
        
        print(f"final Score: {self.PLAYER.NAME}: {self.PLAYER.WINS}, dealer: {self.DEALER.WINS}")
        
        if self.PLAYER.WINS >= 3:
            print(f"{self.PLAYER.NAME} won the match")
        else:
            print("deleaer won the match")

def test_player_class():
    TESTER = Player("Falstaff")
    TESTCARD = Card(12, 3)

    print(TESTER.NAME) 

    print(TESTER.HAND)
    TESTER.take_card(TESTCARD)
    print(len(TESTER.HAND)) 

    print(TESTER.HAND_VALUE)  
    TESTER.set_hand_value(10)
    print(TESTER.HAND_VALUE)  

    print(TESTER.STAND)  
    TESTER.stand_hand()
    print(TESTER.STAND)  

    print(TESTER.WINS) 
    TESTER.add_win()
    print(TESTER.WINS)  

    TESTER.reset_hand()
    print(TESTER.STAND) 
    print(TESTER.HAND)  
    print(TESTER.HAND_VALUE)  


if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()
