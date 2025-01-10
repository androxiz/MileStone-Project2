import random
from CardClass import * 


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

'''
The Deck class represents a standard deck of playing cards.
It is responsible for creating the deck, shuffling it, and dealing cards.

Key functionalities:
- Creating a full deck of 52 cards by combining each suit with each rank.
- Shuffling the deck to randomize the order of the cards.
- Dealing a single card from the deck.
'''

class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create a card by combining each suit with each rank
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
                

    def shuffle(self):
        random.shuffle(self.all_cards)  #Shuffles the deck of cards


    def deal_one(self): #Deals one card from the deck
        return self.all_cards.pop(0)
    