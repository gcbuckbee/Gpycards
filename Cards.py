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
def class Card(Suit, Rank):
    def __init__(Suit, Rank):
        self.faceUp = TRUE
        self.faceDown = FALSE
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
def class CardCollection():
    def __init__():
        self.cards = []
        self.cardCount = 0
        return
        
    def shuffle():
        return

    def sort(Key):
        if Key = "Rank" then
        
        elif Key = "Suit" then
        
        elif Key = "Both" then
        
        return
        
        
    def addCard(cardName)
        self.append(cardName)
        return
        
    def removeCard(index)
        del self[index]
        return
        
    def draw()
    # Drawing on the screen....not to be confused with drawing a card from the deck...
        return
        
# =================================================================================
# Deck Object
# =================================================================================
def class CardCollection() Deck() :
    def __init__():
        # create 52 card deck
        return
        
# =================================================================================
# Hand Object
# =================================================================================
def class CardCollection() Hand:
    def __init__():
        return
        
        
# =================================================================================
# Table Object
# =================================================================================
def class Table():
    def __init__():
        return

# =================================================================================
# Spot Object
# =================================================================================
def class Spot():
    def __init__():

