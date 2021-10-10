class GameStat:
    def __init__(self,id,name,num_plays,num_wins):
        self.__id = id
        self.__name = name
        self.__num_plays = num_plays
        self.__num_wins = num_wins

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def num_plays(self):
        return self.__num_plays

    @num_plays.setter
    def num_plays(self,num_plays):
        self.__num_plays = num_plays

    @property
    def num_wins(self):
        return self.__num_wins

    @num_wins.setter
    def num_wins(self,num_wins):
        self.__num_wins = num_wins

    
    def __str__(self):
        if self.__id == 1:
            return f"{self.__name}: #plays = {self.__num_plays},#wins = {self.__num_wins}"
        else:
            return f"{self.__name}: #plays = {self.__num_plays},#score = {self.__num_wins}"

