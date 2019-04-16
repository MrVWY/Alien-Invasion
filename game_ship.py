import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self, ai_settings,screen):
        """initialization the ship and reset its start position """
        super(Ship,self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(r'C:\Users\ZJL\PycharmProjects\untitled\game_test\airship .bmp')  # load image
        self.rect = self.image.get_rect()  # 返回一个表示飞船的矩形
        self.screen_rect = screen.get_rect()  # 返回一个表示屏幕的矩形


        self.rect.centerx = self.screen_rect.centerx  # 将飞船中心的x坐标设置为表示屏幕的矩形的属性centerx
        self.rect.bottom = self.screen_rect.bottom  # 注意屏幕边缘的表示：top，bottom，left，right
        # 将每艘飞船放置在屏幕底端中央位置，在pygame中，原点（0，0）位于屏幕左上角

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0 :
            self.center -= self.ai_settings.ship_speed_factor
        #根据self.center更新rect对象
        self.rect.centerx=self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # 根据self.rect指定的位置将图像绘制到屏幕中（self.rect就是图像的一个外接矩形）

    def center_ship(self):
        """let the ship between two parties"""
        self.center =self.screen_rect.centerx