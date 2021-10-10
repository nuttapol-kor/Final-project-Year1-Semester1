## About The Project

This project is part of Computer Programming I course (01219114). 
for practicing oop programming in python

There are 3 games in this project:
* Blackjack
* Pok_deng
* Simon memory

### Built With
* [pygame](https://www.pygame.org/)

## Getting Started

### Prerequisites
Things you need to use in this project
* [python](https://www.python.org/)
* pygame
    ```bash
    pip install pygame
    ```
### Installation

1. Clone the repo
    ```bash
    git clone https://github.com/nuttapol-kor/Final-project-Year1-Semester1.git
    ```
2. Change directory to Final-project-Year1-Semester1
    ```bash
    cd Final-project-Year1-Semester1
    ```
3. Run the program
    ```bash
    python main.py
    ```

## Game Rule

### Blackjack rule
1. Each player draw 2 cards.
2. Value of card
The cards that has a number,value is same with that number.
Jack,King,Queen card value = 10
Ace card value depend on if the first 2 cards are drawn has Ace card value = 11
if draw card more after draw the first 2 cards, ace card value = 1
3. If any player who has value = 21 in the first draw, the game will over immediately and 
player who has value = 21 will be a winner. if both player has value = 21 will be tie.
4. If both player value of cards not reach to 21, both player can draw more again and again.
if draw until value over 21 can't draw a card anymore
5. Player who has value nearest 21 will be win
6. If value over 21 will be lose.

### Pok Deng rule
At the start of the game, everyone will draw 2 cards.
The card value of Ace will equal to 1 and 2 and 3 and 4 will equal to their number and so on,
the Jack,King,Queen will equal to 10.
If the card value you received is more than 10, it will divide by 10
For example, if your card value is 15 it will be cut down to 5
If the suit of both card is the same, it will be count as Deng. Same with 3 cards.
Deng means you get 2 times more score.
Same with 3 cards, you will get 3 times more score.
The winner will be the one with the higher cards value.
If , at the start, any of the player got a Pok 8 or Pok 9, other player won't be able to draw more card.
If you draw one more card and all your card is the same value it will be count as Tong.
For example, if you got 2 ace and then you draw one more ace your card will be count as Tong.
If you win by Tong card, you will get 5 times more score.
If you got Jack,King,Queen or basically any card that isn't a number for 3 cards it will be count as Straight Flush.
For example, you got Jack and King then you draw one more and got Jack it will be count as Straight Flush.

### Simon memory rule
At the start of the game, the AI will randomly click on one of the four color in your screen.
The AI will click once on the first round and click 2 times on the second round and so on.
To play this game, you must press on the color that the AI press on.
For example, The AI press red and blue. You must press these color in order to proceed to the next round.
The game will stop when you press wrong once.