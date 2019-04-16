import pygame.font
from pygame.sprite import  Group
from  game_ship import Ship
class Scoreboard():
    """report the scored information"""

    def __init__(self,ai_settings,screen,stats):
        '''Reset and show the score information and attribute'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #set up the score font
        self.text_colour = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #prepare the inital score image , high_score and game lever
        self.preg_score()
        self.preg_high_score()
        self.preg_lever()
        self.preg_ships()

    def preg_score(self):
        """make the score to a image"""
        rounded_score = int(round(self.stats.score,-1))#Round enables decinmal numbers to be precise to how many decimal places after hte decimal point
        score_str = "{:,}".format(rounded_score)
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_colour,self.ai_settings.bg_colour)

        #make the score information in the upper righr corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """show the score in the screen """
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lever_imgae,self.lever_rect)
        self.ships.draw(self.screen)

    def preg_high_score(self):
        high_score = int(round(self.stats.high_score,-1))  # Round enables decinmal numbers to be precise to how many decimal places after hte decimal point
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_colour, self.ai_settings.bg_colour)

        #make the high_score in the top center of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def preg_lever(self):
        """make the game lever to the imgae"""
        self.lever_imgae = self.font.render(str(self.stats.lever),True,self.text_colour,self.ai_settings.bg_colour)

        #Place the game lever below the score
        self.lever_rect = self.lever_imgae.get_rect()
        self.lever_rect.right = self.score_rect.right
        self.lever_rect.top = self.score_rect.bottom + 20

    def preg_ships(self):
        """show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
