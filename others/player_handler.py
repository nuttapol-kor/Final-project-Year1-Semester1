from others.player import Player

class PlayerHandler:
    def __init__(self):
        self.__player = []

    @property
    def player(self):
        return self.__player

    def read_from_file(self,filename):
        file1 = open(filename).read().splitlines()
        for i in file1:
            self.__player.append(i.split(","))

    def write_to_file(self,filename):
        file1 = open(filename,"w")
        for player in self.__player:
            file1.write(f"{player}")

    def show_player(self):
        for player in self.__player:
            print(player)

    def add_new_player(self,player):
        self.__player.append(player)

    def search_player(self,name):
        for player in self.__player:
            if name == player.name:
                return player
    def add_balance(self,name,added):
        p1 = self.search_player(name)
        p1.update_balance(added)
            
