from PlayerClass import *
import os

# Function to clear the console screen (works on both Windows and Unix-based systems)
def clear_console():    
    os.system('cls' if os.name == 'nt' else 'clear')

# Displays the dealer's first card and hide the second one
def show_dealer_card():
    print(f"\n Dealer`s cards: \n{dealer.all_cards[0]}: {dealer.all_cards[0].value}")
    print("<The second card is hidden>")

# Method to handle the player's win and update his bank balance
def player_win(player, value):
    print("You win!\n")
    player.bank += value

# Function to handle the case when the player busts (goes over 21)
def player_busts(player, value):
    print("You bust!\n")
    print("Dealer wins!\n")
    player.bank -= value

# Function to handle the dealer's win and update the player's bank balance
def dealer_win(player, value):
    print("Dealer wins!\n")
    player.bank -= value

# Function to handle the case when the dealer busts (goes over 21)
def dealer_busts(player, value):
    print("Dealer busts!\n")
    print("You win!\n")
    player.bank += value


def tie():
    print("Its a tie!")


# Main game function
def play_game():

    playing = True  # Variable to control the main game loop

    # Main game loop
    while playing:
        clear_console()
        player.all_cards = []
        player.value = 0
        player.aces = 0 

        dealer.all_cards = []
        dealer.value = 0
        dealer.aces = 0

        deck = Deck()
        deck.shuffle()

        # Bet input loop, ensuring the player provides a valid bet
        is_bet_right = False
        while not is_bet_right:
            print(f"\n Your total balance is {player.bank}$")
            try:
                bet_value = int(input("\nMake a bet: "))
                clear_console()
            except:
                clear_console()
                print("\nYou provided an incorrect bet!")
            else:
                is_bet_right = player.bet(bet_value)


        # Deal two cards to both the player and the dealer
        for _ in range(2):
            player.add_card(deck.deal_one())
            dealer.add_card(deck.deal_one())


        # Player's decision-making loop (take or stay)
        p_choise = ''
        while p_choise != "stay":
            print(player)
            show_dealer_card()

            p_choise = input("\nEnter your choise (take/stay): ")
            if p_choise.lower() == "take":
                clear_console()
                player.add_card(deck.deal_one())
                player.adjust_for_ace()
            else:
                clear_console()
                

        if player.value > 21:
            player_busts(player, bet_value)
            
        # If the player hasn't busted, the dealer plays
        if player.value <= 21:
            while dealer.value < 17:
                dealer.add_card(deck.deal_one())
                dealer.adjust_for_ace()

            print(player)
            print(dealer)

            if dealer.value > 21:
                dealer_busts(player, bet_value)
            elif dealer.value > player.value:
                dealer_win(player, bet_value)
            elif player.value > dealer.value:
                player_win(player, bet_value)
            else:
                tie()

        # Display the player's current balance
        print(f"{player.name}, your current balance is {player.bank}$")

        # Ask if the player wants to continue playing
        p_answer = ''
        while p_answer != 'y' and p_answer != 'n':
            p_answer = input("Do you want to continue playing (y/n)?: ")
            if p_answer == 'y':
                playing = True
            elif p_answer == "n":
                print("Thanks for playing!")
                playing = False


if __name__ == "__main__":
    name = input("Enter player`s name: ")
    player = Player(name)

    dealer = Player("Dealer")

    play_game()