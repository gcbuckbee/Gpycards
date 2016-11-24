# ============================================================================================
# cardgame.py
# ============================================================================================
# Shell for testing pycards 
# --------------------------------------------------------------------------------------------
# G. Buckbee
# 2016-Oct-31
# Updated 22-Nov-2016
# ============================================================================================

from Cards import *

testDeck = Deck()
# testDeck.shuffleMe()

testDeck.printCards()
print('---------------')

testHand = Hand()

for i in range(1,5):
    myCard = testDeck.dealCard(0)
    testHand.addCard(myCard)

# testHand.printCards()

print (testDeck.countCards())
print (testHand.countCards())

# print (testCard.rank, ' of ', testCard.suit)
