# Black Jack Game

This is my second Python small milestone project: a simple card game where players can place bets, draw cards, and compete against the dealer without exceeding a total value of 21.

---

## 📋 Description

* The game is played in the console and includes a player and a dealer.

* Players start with a balance of $250 and can place bets before each round.

* Cards are drawn from a shuffled deck, and the goal is to get closer to 21 than the dealer without going over.

* The dealer must draw cards until their total value is at least 17.

* The game ends when the player chooses to stop.

---

## 📑 Project structure

* **CardClass.py:** Describes card classes.

* **DeckClass.py:** Controls deck creation and shuffling.

* **PlayerClass.py:** Defines players and how they interact with the game.

* **GameLogic.py:** Contains the core game logic and user interaction.

---

## 🚀 Features

* **Cards and Deck:** Fully functional deck of 52 cards with shuffling and dealing capabilities.

* **Player and Dealer:** Gameplay includes interaction between a player and a dealer.

* **Bets:** Ability to place bets with balance validation.

* **Ace Adjustment:** Automatic adjustment of Ace value (11 or 1) depending on the current total.

* Gameplay:

  * Player name input.

  * Card dealing.

  * Player choices: draw a card or stay.

  * Dealer's logic for drawing cards.

  *Determining the winner.

* **Balance and Bet Support:** Automatic update of the player's balance after each game.

* **Cross-platform Console Management:** Screen clearing for better display.

* **Console Clearing:** The console is cleared after each move for better readability.
---

## 📚 Technologies Used

* **Programming Language:** Python

* **Libraries:**

  * random: Used for shuffling the deck.

  * os: Used for clearing the console.

---

## 🙏 Acknowledgments

Thank you for reviewing my second milestone project! Feedback and suggestions for improvements are greatly appreciated.
---
