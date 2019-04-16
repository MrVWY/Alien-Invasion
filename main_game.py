import pygame
from games_Setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from games_status import status
from games_button import Button
from games_scoreboard import Scoreboard
def run_game():
    pygame.init()  #初始化背景设置
    ai_settings=Setting()  #实例化
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #调用属性设置屏幕的宽高
    pygame.display.set_caption("Alien Invasion")  #设置标题
    play_button = Button(ai_settings,screen,"Play")#Establish a play_button button
    ship=Ship(ai_settings,screen)  #实例化Ship self会把ai_settings,screen跟随着ship
    bullets = Group() #创建一个存储bullet的编组
    #alien = Alien(ai_settings,screen)#创建一个alien
    aliens = Group()
    #create alien
    gf.create_many_alien(ai_settings,screen,ship,aliens)
    #eatablish a stockpile game statistics
    stats = status(ai_settings)
    sb  = Scoreboard(ai_settings,screen,stats)
    while True:
        gf.check_events(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        if stats.game_active:
           ship.update()  #update the ship's related attributes
           gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)#update the munber of bullets
           gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)#update the alien location ,numbers
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)#update the alien, the ship,the bullets


run_game()