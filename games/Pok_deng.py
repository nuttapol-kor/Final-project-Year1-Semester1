import sys
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
        self.__real_val = 0
        self.__hit = 1
        self.__pok8 = False
        self.__pok9 = False
        self.__straight_flush = False
        self.__tong = False
    @property
    def hand(self):
        return self.__hand

    @property
    def val(self):
        return self.__val

    @property
    def real_val(self):
        return self.__real_val
    
    @property
    def hit(self):
        return self.__hit
    
    @property
    def pok8(self):
        return self.__pok8

    @property
    def pok9(self):
        return self.__pok9

    @property
    def tong(self):
        return self.__tong

    @property
    def straight_flush(self):
        return self.__straight_flush

    @val.setter
    def val(self,val):
        self.__val = val

    @real_val.setter
    def real_val(self,real_val):
        self.__real_val = real_val

    @hit.setter
    def hit(self,hit):
        self.__hit = hit
    
    def draw_cards(self,deck, n):
        """
        just draw a card, when you draw a card that card will move from the deck to you hand,
        that mean the card from deck disappear by drawing.
        """
        for _ in range(n):
            self.__hand.append(deck.pop())

    def display_cards(self):
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
        
        for i in display_str:
            print(i,end="")
        print("")

    def calculate_hand_value(self):
        """
        culculate the vulue form card
        """
        for card in self.__hand:
            ltemp = card.split()
            if ltemp[0] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                self.__val += int(ltemp[0])
            elif ltemp[0] in ['Jack', 'Queen', 'King']:
                self.__val += 10
            elif ltemp[0] in ['Ace']:
                self.__val += 1

        if self.__val >= 10:
            self.__real_val += self.__val % 10

        else:
            self.__real_val += self.__val
        
    def calcuate_suit(self):
        """
        calcuate suit cards in hand 
        """
        suit = []
        for card in self.__hand:
            ltemp = card.split()
            suit.append(ltemp[1])
        nTemp = suit[0]
        bEqual = True
        for i in suit:
            if nTemp != i:
                bEqual = False
                break
        if bEqual:
            self.__hit = len(suit)

    def check_pok8(self):
        """
        check pok 8 from cards in each hand
        """
        if self.__real_val == 8:
            self.__pok8 = True
    
    def check_pok9(self):
        """
        check pok 9 from cards in each hand
        """
        if self.__real_val == 9:
            self.__pok9 = True

    def add_more_card(self,deck):
        """
        this function will return True when you want to draw more card, and will return False when
        you not want to draw anymore.
        """
        while True:
            do = input("Draw More?(Yes/No): ")
            do.lower()
            if do == "yes":
                self.draw_cards(deck,1)
                break
            elif do == "no":
                break
            else:
                print("Invalid Choice")
            
    def check_straight_flush_and_tong(self):
        """
        check straight flush and tong and set True when it is
        """
        blank_list = []
        num = 0
        for card in self.__hand:
            ltemp = card.split()
            blank_list.append(ltemp[0])
        for i in blank_list:
            if i in ['Jack', 'Queen', 'King']:
                num += 1
        if len(blank_list) == num:
            self.__straight_flush = True

        nTemp = blank_list[0]
        bEqual = True
        for i in blank_list:
            if nTemp != i:
                bEqual = False
                break
        if bEqual:
            self.__tong = True
        
    def bot_fight(self,deck):
        """
        bot will draw more when cards in hand less than 4
        """
        if self.__real_val < 4:
            self.draw_cards(deck,1)

    def reset(self):
        """
        set attributes like when game start
        """
        self.__hand = []
        self.__val = 0
        self.__real_val = 0
        self.__hit = 1
        self.__pok8 = False
        self.__pok9 = False
        self.__straight_flush = False
        self.__tong = False


class Pok_Deng:
    def __init__(self,player):
        """
        Initializing player
        """
        self.__player = player

    def play(self):
        """
        play the game
        """
        playing = True

        while playing:
            # initialze a deck of cards
            self.deck = Deck()
            # shuffle the deck
            self.deck.shuffle_cards()

            #draw a player hand
            self.player_hand = Hand()
            self.player_hand.draw_cards(self.deck.deck,2)

            #draw the computer hand
            self.computer_hand = Hand()
            self.computer_hand.draw_cards(self.deck.deck,2)
            self.player_hand.calcuate_suit()
            self.computer_hand.calcuate_suit()
            # display player_hand
            print(f"{self.__player.name} hand: ", end = '')
            self.player_hand.display_cards()
            print(f"{self.player_hand.hit} Deng")
            # # display computer_hand
            # print("Computer hand: ", end = '')
            # self.computer_hand.display_cards()

            #calculate value
            self.player_hand.calculate_hand_value()
            self.computer_hand.calculate_hand_value()
            # self.player_hand.real_val
            # self.computer_hand.real_val
            # print(f"Player val: {self.player_hand.real_val}")
            # print(f"Com val: {self.computer_hand.real_val}")
            
            #check pok
            self.player_hand.check_pok8()
            self.computer_hand.check_pok8()
            self.player_hand.check_pok9()
            self.computer_hand.check_pok9()


            if self.player_hand.pok9 and self.computer_hand.pok9:
                print("Both tie")
            elif self.player_hand.pok9:
                print(f"{self.__player.name} wins")
                self.__player.update_num_wins(3,1*self.player_hand.hit)
            elif self.computer_hand.pok9:
                print("Computer wins")

            if self.player_hand.pok8 and self.computer_hand.pok8:
                print("Both tie")
            elif self.player_hand.pok8:
                print(f"{self.__player.name} wins")
                self.__player.update_num_wins(3,1*self.player_hand.hit)
            elif self.computer_hand.pok8:
                print("Computer wins")

            if self.player_hand.pok9 or self.computer_hand.pok9 or self.player_hand.pok8 or self.computer_hand.pok8:
                print("Computer hand: " , end="")
                self.computer_hand.display_cards()
                print(f"{self.computer_hand.hit} Deng")
                break

            #draw 3 cards
            self.player_hand.add_more_card(self.deck.deck)
            if self.computer_hand.real_val < 4:
                self.computer_hand.draw_cards(self.deck.deck,1)

            self.player_hand.hit = 1
            self.computer_hand.hit = 1

            self.player_hand.calcuate_suit()
            self.computer_hand.calcuate_suit()

            print(f"{self.__player.name} hand: ", end = '')
            self.player_hand.display_cards()
            print(f"{self.player_hand.hit} Deng")
            # print("Computer hand: ", end = '')
            # self.computer_hand.display_cards()

            #reset val for calculate again
            self.player_hand.val = 0
            self.player_hand.real_val = 0
            self.computer_hand.val = 0
            self.computer_hand.real_val = 0

            self.player_hand.calculate_hand_value()
            self.computer_hand.calculate_hand_value()
            self.player_hand.val
            self.player_hand.real_val
            self.computer_hand.val
            self.computer_hand.real_val

            self.player_hand.check_straight_flush_and_tong()
            self.computer_hand.check_straight_flush_and_tong()

            # print(self.player_hand.real_val)
            # print(self.computer_hand.real_val)
            #check tong

            self.player_hand.real_val
            self.computer_hand.real_val
            if self.player_hand.tong and self.computer_hand.tong:
                print("Both tie")
            elif self.player_hand.tong:
                print(f"{self.__player.name} wins")
                self.__player.update_num_wins(3,5)
            elif self.computer_hand.tong:
                print("Computer wins")
            if self.player_hand.tong or self.computer_hand.tong:
                print("Computer hand: " , end="")
                self.computer_hand.display_cards()
                print(f"{self.computer_hand.hit} Deng")
                break
            
            self.player_hand.real_val
            self.computer_hand.real_val
            if self.player_hand.straight_flush and self.computer_hand.straight_flush:
                print("Both tie")
            elif self.player_hand.straight_flush:
                print(f"{self.__player.name} wins")
                self.__player.update_num_wins(3,3)
            elif self.computer_hand.straight_flush:
                print("Computer wins")
            if self.player_hand.straight_flush or self.computer_hand.straight_flush:
                print("Computer hand: " , end="")
                self.computer_hand.display_cards()
                print(f"{self.computer_hand.hit} Deng")
                break
            
            self.player_hand.real_val
            self.computer_hand.real_val

            if self.player_hand.real_val == self.computer_hand.real_val:
                print("Both tie")
                print("Computer hand: " , end="")
                self.computer_hand.display_cards()
                print(f"{self.computer_hand.hit} Deng")
                break
            elif self.player_hand.real_val > self.computer_hand.real_val:
                print(f"{self.__player.name} wins")
                self.__player.update_num_wins(3,1*self.player_hand.hit)
                print("Computer hand: " , end="")
                self.computer_hand.display_cards()
                print(f"{self.computer_hand.hit} Deng")
                break
            elif self.player_hand.real_val < self.computer_hand.real_val:
                print("Computer wins")
                print("Computer hand: " , end="")
                self.computer_hand.display_cards()
                print(f"{self.computer_hand.hit} Deng")
                break
        self.__player.update_num_plays(3)
        self.__player.update_balance(-10)
    
            
                
            
            
            
# import sys
# d = Deck()
# d.shuffle_cards()
# # print(d.deck)
# p1 = Hand()
# p1.draw_cards(d.deck,2)
# print(f"player hand: {p1.hand}")
# p1.display_cards()
# p1.calculate_hand_value()
# print(f"player val: {p1.val}")
# print(f"player real val: {p1.real_val}")
# p1.calcuate_suit()
# p1.check_pok()
# print(f"Pok : {p1.pok}")
# print(f"player hit: {p1.hit}")
# if p1.pok:
#     sys.exit()
# else:
#     p1.add_more_card()

# game = Pok_Deng()
# game.play() 