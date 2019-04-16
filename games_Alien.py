import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    '''表示单个外星人'''
    def __init__(self,ai_settings,screen):
        """设置起始位置"""
        super(Alien, self).__init__()
        self.screen=screen
        self.ai_settings = ai_settings

        #加载alien图像，设置rect属性
        self.image = pygame.image.load(r'C:\Users\ZJL\PycharmProjects\untitled\game_test\Alien.bmp')
        self.rect = self.image.get_rect()

        #每个alien最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """if alien's location is thr edges of screen ,return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return  True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """trun right or trun left to move the alien"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

