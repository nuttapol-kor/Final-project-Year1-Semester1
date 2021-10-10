from others.game_stat import GameStat
class Player:
    def __init__(self,name,balance=0):
        self.__name = name
        self.__balance = balance
        self.__game_stat_list = [GameStat(1,"Blackjack",0,0),GameStat(2,"Simon_memory",0,0),GameStat(3,"Pok_Deng",0,0)]
    
    def __str__(self):
        game_stat_str = ""
        for i in self.__game_stat_list:
            game_stat_str += f"{i}\n"
            
        return f"{self.__name}: Balance = {self.__balance:.2f}\n"+game_stat_str
    
    def find_game_stat(self,game_id):
        return self.__game_stat_list[game_id-1]

    def update_num_plays(self,game_id):
        self.find_game_stat(game_id).num_plays += 1

    def update_num_wins(self,game_id,win_value):
        self.find_game_stat(game_id).num_wins += win_value

    def update_balance(self,balance):
        self.__balance += balance

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def balance(self):
        return self.__balance
    
    # @balance.setter
    # def balance(self,balance):
    #     self.__balance = balance
    
