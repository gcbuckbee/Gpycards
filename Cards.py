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

# =================================================================================
# Card Object
# =================================================================================
class Card:
    def __init__(self, Rank, Suit):
        self.faceUp = True
        self.faceDown = False
        self.suit = Suit
        self.rank = Rank
        self.color = "Black"
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
    def __init__():
        self.cards = []
        self.cardCount = 0
        return
        
    def shuffle():
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
    def __init__():
        # create 52 card deck
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

