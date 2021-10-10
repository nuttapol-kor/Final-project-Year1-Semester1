class Deck:
    def __init__(self):
        """
        Initialzing a deck for play
        """
        self.__rank = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        self.__suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.__deck = []
        for rank in self.__rank:
            for suit in self.__suit:
                card = rank + ' ' + suit
                self.__deck += [card]
    @property
    def deck(self):
        return self.__deck

    def shuffle_cards(self):
        """
        shuffle the deck before playing blackjack
        """
        import random
        n = len(self.__deck)
        for i in range(n):
            r = random.randrange(i, n)
            temp = self.__deck[r]
            self.__deck[r] = self.__deck[i]
            self.__deck[i] = temp

class Hand:
    def __init__(self):
        """
        Initializing hand/ val / etc. use for play
        """
        self.__hand = []
        self.__val = 0
        self.__num_ace = 0
        self.__STAY_VAL = 16
        self.__must_draw_bool = False
        self.__add_more_card_bool = False
    def get_hand(self):
        return self.__hand
    def get_val(self):
        return self.__val
    def set_val(self,val):
        self.__val = val
    def get_must_draw_bool(self):
        return self.__must_draw_bool
    def get_add_more_card_bool(self):
        return self.__add_more_card_bool

    def draw_cards(self,deck, n):
        """
        just draw a card, when you draw a card that card will move from the deck to you hand,
        that mean the card from deck disappear by drawing.
        """
        for _ in range(n):
            self.__hand.append(deck.pop())

    def display_cards(self,final=False):
        """
        show the cards in the hand with suit symbol 
        """
        display_str = []
        for each_card in self.__hand:
            ltemp = each_card.split()
            if ltemp[1] == 'Clubs':
                display_str += [ltemp[0] + '\u2663' + ' ']
            elif ltemp[1] == 'Diamonds':
                display_str += [ltemp[0] + '\u2666' + ' ']
            elif ltemp[1] == 'Hearts':
                display_str += [ltemp[0] + '\u2665' + ' ']
            else:
                assert ltemp[1] == 'Spades', 'Spades expected'
                display_str += [ltemp[0] + '\u2660' + ' ']
        if final:
            for i in display_str[1:]:
                print(i,end="")
            print("")
        else:
            for i in display_str:
                print(i,end="")
            print("")

    def calculate_hand_value(self):
        """
        Return the value of a given hand. When there are Ace rank cards in the hand, use the max value of Ace rank, which is 11 - 1 + the number of all Ace rank cards, if the resulting hand value is not greater than 21; otherwise, use the min value of Ace rank, which is the number of all Ace rank cards.
        >>> f = Hand()
        >>> f.__hand = ['5 Hearts', '7 Diamonds', '3 Clubs', '8 Spades']
        >>> calculate_hand_value()
        >>> f.__val
        23
        """
        for card in self.__hand:
            ltemp = card.split()
            if ltemp[0] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                self.__val += int(ltemp[0])
            elif ltemp[0] in ['Jack', 'Queen', 'King']:
                self.__val += 10
            else:
                assert ltemp[0] == 'Ace', 'Ace rank expected'
                self.__num_ace += 1
        if self.__num_ace == 0:
            pass
        else:
            if (self.__val + self.__num_ace - 1 + 11) > 21:
                self.__val = self.__val + self.__num_ace
            else:
                self.__val = self.__val + self.__num_ace - 1 + 11


    def check_for_Blackjack(self):
        """Return True if a given hand is a Blackjack, return False, otherwise.

        """
        assert len(self.__hand) == 2, 'Blakjack hand must contain exactly two cards.'
        if self.__val == 21:
            return True
        else:
            return False

    def must_draw_more(self):
        """Return True if a given hand value is not enough to stay, return False, otherwise.
    
        """
        if self.__val < self.__STAY_VAL:
            self.__must_draw_bool = True
        else:
            self.__must_draw_bool = False

    def add_more_card(self):
        """
        this function will return True when you want to draw more card, and will return False when
        you not want to draw anymore.
        """
        while True:
            do = input("Draw More?(Yes/No): ")
            do.lower()
            if do == "yes":
                self.__add_more_card_bool = True
                break
            elif do == "no":
                self.__add_more_card_bool = False
                break
            else:
                print("Invalid Choice")


class Blackjack:
    def __init__(self,player):
        """
        Initialzing player
        """
        self.__player_wins = False
        self.__player = player

    @property
    def player_wins(self):
        return self.__player_wins

    @player_wins.setter
    def player_wins(self,player_wins):
        self.__player_wins = player_wins

    @property
    def player(self):
        return self.__player

    def play(self):
        """
        play the game
        """
        playing = True

        while playing:
            # initialize a deck of cards
            self.deck = Deck()
            # shuffle the deck
            self.deck.shuffle_cards()

            # draw a player hand
            self.player_hand = Hand()
            self.player_hand.draw_cards(self.deck.deck,2)

            # draw the computer hand
            self.computer_hand = Hand()
            self.computer_hand.draw_cards(self.deck.deck,2)

            # display player_hand
            print(f"{self.__player.name} hand: ", end = '')
            self.player_hand.display_cards()

            # display computer_hand
            print("Computer hand: ", end = '')
            self.computer_hand.display_cards(True)


            # check if decision can be made right away with Blackjack hands
            self.player_hand.calculate_hand_value()
            self.player_hand.get_val()
            self.computer_hand.calculate_hand_value()
            self.computer_hand.get_val()

            if self.player_hand.check_for_Blackjack() and self.computer_hand.check_for_Blackjack():
                print("Both tie")
            elif self.player_hand.check_for_Blackjack():
                print(f"{self.__player.name} wins")
                self.__player.update_num_wins(1,1)
                self.player_wins = True
            elif self.computer_hand.check_for_Blackjack():
                print("Computer wins")

            if self.player_hand.check_for_Blackjack() or self.computer_hand.check_for_Blackjack():
                print("Computer hand: " , end="")
                self.computer_hand.display_cards()
                self.computer_hand.get_val()
                break
                
                

            # player must draw more cards if hand value is below the threshold
            self.player_hand.must_draw_more()
            while self.player_hand.get_must_draw_bool():
                self.player_hand.draw_cards(self.deck.deck,1)
                print(f"{self.__player.name} hand: ", end = '')
                self.player_hand.display_cards()
                self.player_hand.set_val(0)
                self.player_hand.calculate_hand_value()
                self.player_hand.get_val()
                self.player_hand.must_draw_more()
            
            # computer must draw more cards if hand value is below the threshold
            self.computer_hand.must_draw_more()
            while self.computer_hand.get_must_draw_bool():
                self.computer_hand.draw_cards(self.deck.deck,1)
                print("Computer hand: ", end = '')
                self.computer_hand.display_cards(True)
                self.computer_hand.set_val(0)
                self.computer_hand.calculate_hand_value()
                self.computer_hand.get_val()
                self.computer_hand.must_draw_more()

            #chioce to draw a card more
            self.player_hand.add_more_card()
            while self.player_hand.get_add_more_card_bool():
                self.player_hand.draw_cards(self.deck.deck,1)
                print(f"{self.__player.name} hand: ", end = '')
                self.player_hand.display_cards()
                self.player_hand.add_more_card()
            
            # determine who wins or they are both tie
            self.player_hand.set_val(0)
            self.player_hand.calculate_hand_value()
            self.computer_hand.set_val(0)
            self.computer_hand.calculate_hand_value()
            player_stand = self.player_hand.get_val()
            computer_stand = self.computer_hand.get_val()

            if player_stand > 21:
                if computer_stand > 21:
                    print("Both tie")
                else:
                    print("Computer wins")
            else:
                if computer_stand > 21:
                    print(f"{self.__player.name} wins")
                    self.__player.update_num_wins(1,1)
                    self.player_wins = True
                else:
                    # the computer can fight back as it knows what the hand value for player is
                    while computer_stand < player_stand:
                        self.computer_hand.draw_cards(self.deck.deck,1)
                        self.computer_hand.set_val(0)
                        self.computer_hand.calculate_hand_value()
                        computer_stand = self.computer_hand.get_val()
                        print("Computer hand adjusted: ", end = '')
                        self.computer_hand.display_cards(True)
                    if computer_stand > 21:
                        print(f"{self.__player.name} wins")
                        self.__player.update_num_wins(1,1)
                        self.player_wins = True
                    elif computer_stand == player_stand:
                        print("Both tie")
                    else:
                        print("Computer wins")
            print("Computer hand final: ", end="")
            self.computer_hand.display_cards()
            self.computer_hand.get_val()
            break

        self.__player.update_num_plays(1)
        self.__player.update_balance(-10)

