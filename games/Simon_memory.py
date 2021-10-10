import pygame
from random import randint
from time import sleep

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]


class Button:
    def __init__(self, color, pos, screen):
        """
        Initializing material for Botton
        """
        self.__color = color
        self.__pos = pos
        self.__shape = 0
        self.__grid_line = [((450,0),(450,450))]
        self.__screen1 = screen
        self.draw()


    def draw(self):
        """
        draw the botton and line
        """
        self.__shape = pygame.draw.rect(self.__screen1, self.__color, self.__pos)
        for line in self.__grid_line:
            pygame.draw.line(self.__screen1, (255,255,255),line[0],line[1],2)

    def dark(self):
        """
        change botton color to dark
        """
        index = 0
        for i in self.__color:
            if i == 255:
                i -= 95
                self.__color[index] = i
            index += 1
        self.draw()
        pygame.display.update()

    def light(self):
        """
        change botton color to normal
        """
        index = 0
        for i in self.__color:
            if i == 160:
                i += 95
                self.__color[index] = i
            index += 1
        self.draw()
        pygame.display.update()

    def dark_to_light(self):
        """
        change botton color
        """
        self.dark()
        sleep(.5)
        self.light()

class Simon:
    def __init__(self,player):
        """
        Initializing game such as screen,font,botton,player
        """
        self.__width = 600
        self.__height = 450
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__correct_list = []
        self.__player_list = []
        self.__font_name = pygame.font.match_font('comicsans')
        self.__Bot_turn = True
        self.__player_turn = False
        self.__LOSE = False
        self.__score = 0
        self.__running = True
        self.__red_square = Button(red, (25, 25, 200, 200),self.__screen)
        self.__green_square = Button(green, (225, 25, 200, 200),self.__screen)
        self.__blue_square = Button(blue, (25, 225, 200, 200),self.__screen)
        self.__yellow_square = Button(yellow, (225, 225, 200, 200),self.__screen)
        self.__player = player
        pygame.display.update()

    @property
    def player(self):
        return self.__player
    def player_click(self):
        """
        chack when player click
        """
        pos = pygame.mouse.get_pos()
        if (25 < pos[0] < 225) and (25 < pos[1] < 225):
            self.after_click(0)
            self.__player_list.append(0)
        elif (225 < pos[0] < 425) and (25 < pos[1] < 225):
            self.after_click(1)
            self.__player_list.append(1)
        elif (25 < pos[0] < 225) and (225 < pos[1] < 425):
            self.after_click(2)
            self.__player_list.append(2)
        elif (225 < pos[0] < 425) and (225 < pos[1] < 425):
            self.after_click(3)
            self.__player_list.append(3)

    def after_click(self,index):
        """
        change the color when click
        """
        if index == 0:
            self.__red_square.dark_to_light()
        elif index == 1:
            self.__green_square.dark_to_light()
        elif index == 2:
            self.__blue_square.dark_to_light()
        elif index == 3:
            self.__yellow_square.dark_to_light()

    def draw_text(self,surf, text, size, x, y):
        """
        write text
        """
        font = pygame.font.Font(self.__font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def disappear_text(self):
        """
        create black box to hide the text
        """
        pygame.draw.rect(self.__screen, (0, 0, 0), (0, 0, 450, 25))

    def bot_turn(self):
        """
        bot show the botton that should click
        """
        index = randint(0, 3)
        self.__correct_list.append(index )
        for i in self.__correct_list:
            self.after_click(i)
            sleep(.15)
        self.__Bot_turn = False
        self.__player_turn = True

    def check(self):
        """
        if num player click equal num bot click return True
        """
        if len(self.__correct_list) == len(self.__player_list):
            if self.__correct_list == self.__player_list:
                return True
            else:
                self.__LOSE = True
                return False

    def play(self):
        """
        play game
        """
        pygame.init()
        pygame.display.set_caption('Simon memory')
        sleep(1)
        while self.__running:
            if self.__Bot_turn:
                self.disappear_text()
                self.draw_text(self.__screen, 'SIMON\'S TURN', 20, 225, 2, )
                pygame.display.update()
                sleep(.5)
                self.bot_turn()
            if self.__player_turn:
                self.disappear_text()
                self.draw_text(self.__screen, 'PLAYER\'S TURN', 20, 225, 2, )
                pygame.display.update()
                for event in pygame.event.get():
                    if not self.__LOSE:
                        if event.type == pygame.QUIT:
                            self.__running = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            self.player_click()
                            if self.check():
                                self.__Bot_turn = True
                                self.__player_turn = False
                                self.__player_list = []
                                self.__score += 1
                                break
                    else:
                        break            
            if self.__LOSE:
                    break
            
        self.draw_text(self.__screen, 'YOU LOSE!!', 20, 500, 200)
        self.draw_text(self.__screen, 'SCORE:', 20, 500, 225)
        self.draw_text(self.__screen, str(self.__score), 20, 500, 255)
        self.__player.update_num_plays(2)
        self.__player.update_num_wins(2,self.__score)
        self.__player.update_balance(-20)
        pygame.display.update()
        sleep(2)
        pygame.quit()


# game = Simon()
# game.play()