# ---------------------------------------------------------------------------------
# Created 2016-Dec-05
# G. Buckbee
# ---------------------------------------------------------------------------------
# Card Test Routines
# Various test functions to verify operation of card objects:
#   
# ---------------------------------------------------------------------------------
from Cards import *

def test_all_card_objects(print_results):
    passed_test_deck = test_deck(print_results)
    passed_test_flush = test_flush(print_results)

    passed_all_tests = passed_test_deck & passed_test_flush
    return passed_all_tests

# =================================================================================
# TestDeck
# Create a deck of cards, shuffle them and print
# =================================================================================


def test_deck(print_results):
    testDeck = Deck()
    testDeck.shuffle_cards()
    if print_results:
        print('------------------------')
        print('Start of TestDeck()')
        print('Printing a shuffled deck')
        print('------------------------')

        testDeck.print_cards()

    if print_results:
        print('------------------------')
        print('End of TestDeck()')
        print('------------------------')

    test_deck_passed =(testDeck.count_cards() == 52)

    return test_deck_passed


def test_flush(print_results):
    if print_results:
        print('------------------------')
        print('Start of TestFlush()')
        print('------------------------')

    testHand = Hand()

    for i in range(0,5):
        myCard = Card('Six', 'Clubs')
        testHand.addCard(myCard)

    if print_results:
        testHand.printCards()
        print ('Flush evaluation = ', testHand.containsFlush())
        print('------------------------')
        print('End of TestFlush()')
        print('------------------------')

    return testHand.containsFlush()


def TestNoFlush():
    print('------------------------')
    print('Start of TestNoFlush()')
    print('------------------------')

    testHand = Hand()

    for i in range(0,4):
        myCard = Card('Six', 'Clubs')
        testHand.addCard(myCard)

    testHand.addCard(Card('Six', 'Hearts'))

    testHand.printCards()
    print ('Flush evaluation = ', testHand.containsFlush())
    print('------------------------')
    print('End of TestNoFlush()')
    print('------------------------')

    return
