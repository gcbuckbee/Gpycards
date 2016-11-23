# ---------------------------------------------------------------------------------
# Created 2016-Oct-31
# G. Buckbee
# ---------------------------------------------------------------------------------
# Card Game Objects, including:
#   * Card
#   * Card Collection (parent of:)
#      * Deck
#      * Hand
#   * Table
#   * Spot (a location on the table where cards can be shown)
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
from random import shuffle


# =================================================================================
# Card Object
# =================================================================================
class Card:
    def __init__(self, Rank, Suit):
        self.faceUp = True
        self.faceDown = False
        self.suit = Suit
        self.rank = Rank
        if self.suit == "Clubs" or self.suit == "Spades":
            self.color = "Black"
        else:
            self.color = "Red"
        return
        
    def flip():
        return
        
    def draw():
        return
        

# =================================================================================
# Card Collection Object
#   A collection of cards, in sequence
# =================================================================================
class CardCollection:
    def __init__(self):
        self.cards = []
        self.cardCount = 0
        return
        
    def shuffleMe(self):
        shuffle(self.cards)
        return

    def sort(Key):
        if Key == "Rank":
            # sort based on Rank
            print('Rank sort')
        elif Key == "Suit":
            # sort based on Suit
            print('Suit sort')
        elif Key == "Both":
            print('Both sort')
            # sort based on both ranks and suit
            # (A234 of spades, then clubs, the hearts, then diamonds
            
        return

    def printCards(self):
        for card in self.cards:
            eachCard = card
            print(eachCard.rank, "of", eachCard.suit)        
        
    def addCard(cardName):
        self.append(cardName)
        return
        
    def removeCard(index):
        del self[index]
        return
        
    def draw():
    # Drawing on the screen....not to be confused with drawing a card from the deck...
        return
        
# =================================================================================
# Deck Object
# =================================================================================
class Deck(CardCollection) :
    def __init__(self):
        # create 52 card deck
        ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
        suits = ('Clubs', 'Hearts', 'Spades', 'Diamonds')
        self.cards = []
        for suit in suits:
            for rank in ranks:
                newCard = Card(rank, suit)
                self.cards.append(newCard)
                
        return


        return
        
# =================================================================================
# Hand Object
# =================================================================================
class Hand(CardCollection):
    def __init__():
        return
        
        
# =================================================================================
# Table Object
# =================================================================================
class Table():
    def __init__():
        return

# =================================================================================
# Spot Object
# =================================================================================
class Spot():
    def __init__():
        return

