import pygame
from pygame.sprite  import Sprite

class Bullet(Sprite):
    """对飞船发射的子弹进行设置"""

    def __init__(self,ai_setting,screen,Ship):
        super(Bullet,self).__init__() #继承和修改父类Sprite
        self.screen=screen

        #在（0，0）处创建一个表示子弹的矩形，在设置正确的位置
        self.rect=pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx=Ship.rect.centerx
        self.rect.top=Ship.rect.top
        #储存小数表示的子弹位置
        self.y=float(self.rect.y)

        self.colour = ai_setting.bullet_colour
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -=self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.y=self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen,self.colour,self.rect)


