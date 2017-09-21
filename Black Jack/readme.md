## BlackJack.py
A program that when ran, lets the user play a simple game of black jack with standard rules. This is my first program after learning python.

### How it's built
The game starts by creating a list of values from 1 to 53 (exclusive) with the built-in python function `range()`. This sets up the deck. Then using the `random.shuffle()` function to shuffle the deck. A simple dictionary for the cards is used to translate what number corresponds to what card. The suits are left out becuase it seems that suits don't matter much in blackjack, and it made it simpler to code. 

To deal a card, a list for both the dealer and the player is created, then the card in the first position of the deck is appended to one of the hands, and then the first card is deleted from the deck. This is used whenever a card needs to be dealt. 

After hiding the first card of the dealer, and showing the player their cards as well as the dealer's second card, you can choose "check or hit". 
- At any point if you choose check, the dealer will play under the standard rules that he needs to hit on anything lower than 17. Then if you end up with a better hand, or the dealer busts, you win and it will ask if you would like to play again. 
- If you choose hit, it will deal another card for you, and if you bust, it will indicate this and ask if you would like to play again.

Calculating the value of the cards is done by one function for any hand supplied as an argument. It loops through each card in the hand and counts face cards as 10 then aces as 11 because at the end of the loop, it has an aceCount variable that is used to reduce the value of the hand if it would bust and some aces are in the hand.

At then end of the program, it will ask if you would like to play again, if you choose yes, it calls the start function defined at the beginning of the program to loop back through.
