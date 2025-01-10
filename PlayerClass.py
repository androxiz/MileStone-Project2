from DeckClass import *

'''
The Player class represents a player in a card game.
It handles the player's name, their hand of cards, the total value of the cards, 
and their bank balance.

Key functionalities:
- Adding cards to the player's hand and updating the total hand value.
- Accepting and validating bets made by the player.
- Adjusting for aces (changing their value from 11 to 1 if the total exceeds 21).
- Displaying the player's hand and total value.
'''

class Player():

    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.bank = 250
        self.value = 0
        self.aces = 0   # Counter for the number of aces in the player's hand


    # Method to add a card to the player's hand and adjust the total value
    def add_card(self, card):
        self.all_cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    # Method to handle the player's bet, checking if it's valid
    def bet(self, value):
        if self.bank < value:
            print("The player doesn`t have enough money!")
            return False
        elif value < 0:
            print("The bet cant be less than 0")
            return False
        else:
            print("The bet accepted!")
            print(f"Player {self.name} make a bet {value}$")
            return True

    # Method to adjust the value of the hand if the total exceeds 21 and there are aces
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 


    # Method to represent the player's hand as a string
    def __str__(self):
        result = f'\n {self.name}`s cards: \n'  # Display the player's name and cards
        for i in self.all_cards:     # Iterate through each card in the player's hand
            result += f"{i}: {i.value} \n"   # Add each card's rank and value to the result
        
        result +=  f"\nTotal value: {self.value} \n"    # Add the total value of the player's hand
        return result
