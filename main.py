from games.Blackjack import *
from games.Simon_memory import *
from games.Pok_deng import *
from others.game_stat import GameStat
from others.player import Player
from others.player_handler import PlayerHandler
import sys
player_handler = PlayerHandler()
def create_player():
    player_name = input("Enter your name: ")
    name_list = []
    if player_handler.player != []:
        for player in player_handler.player:
            name_list.append(player.name)
        if player_name in name_list:
            for play in player_handler.player:
                if play.name == player_name:
                    player = play
        else:
            player = Player(player_name, 1000)
            player_handler.add_new_player(player)
    else:
        player = Player(player_name, 1000)
        player_handler.add_new_player(player)
    return player


while True:
    status = input("Enter your status (admin/player): ")
    if status == "admin":
        while True:
            print("")
            print("Select your choice")
            print("1. Add new player")
            print("2. Show players")
            print("3. Add player's balance")
            print("4. Quit")
            admin_choice = input("Your choice: ")
            if admin_choice == "1":
                player = create_player()
            elif admin_choice == "2":
                player_handler.show_player()
            elif admin_choice == "3":
                player_name = input("Enter player's name: ")
                balance = float(input("Enter player's added balance: "))
                player_handler.add_balance(player_name, balance)
            elif admin_choice == "4":
                back_or_quit = input("Back to Main or Quit (M/Q): ")
                if back_or_quit in ["M","m"]:
                    break
                elif back_or_quit in ["Q","q"]:
                    sys.exit()
                

    elif status == "player":
        player = create_player()
        while True:
            print("")
            print("Select your choice")
            print("1. Play Blackjack")
            print("2. Play Simon memory")
            print("3. Play Pok deng")
            print("4. See your profile")
            print("5. Stop playing")
            choice = input("Your choice: ")
            if choice == "1":
                print("")
                print(f"Welcome to Blackjack")
                blackjack = Blackjack(player)
                blackjack.play()
            elif choice == "2":
                print("")
                print(f"Welcome to Simon memory")
                simon = Simon(player)
                simon.play()
            elif choice == "3":
                print("")
                print(f"Welcome to Pok Deng")
                pok_deng = Pok_Deng(player)
                pok_deng.play()
            elif choice == "4":
                print(player)
            elif choice == "5":
                player_handler.write_to_file("texts/data.txt")
                break
        back_or_quit = input("Back to Main or Quit (M/Q): ")
        if back_or_quit in ["M","m"]:
            continue
        elif back_or_quit in ["Q","q"]:
            print("Thanks for playing")
            break
    else:
        print("Wrong Input")