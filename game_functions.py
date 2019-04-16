import sys
import pygame
from games_bullet import  Bullet
from games_Alien import Alien
from time import sleep
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True  # 若按下右箭头则使ship.rect.centerx加1
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  # 注意这里若同时按下左右箭头将检测到两个不同事件
    elif event.key == pygame.K_SPACE:
        #判断bullets编组中子弹数量是否有3个（这里保证屏幕上子弹只出现三个）
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    """if not arrive the limi of bullets , shot a bullet"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False  # 若松开右箭头则停止ship.rect.centerx加1
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    for event in pygame.event.get():  #检测键盘鼠标事件
            if event.type==pygame.QUIT:
                sys.exit() #退出程序
            elif event.type==pygame.KEYDOWN:
                check_keydown_events(event, ai_settings,screen,ship,bullets)
            elif event.type==pygame.KEYUP:
                check_keyup_events(event, ship)
            elif event.type == pygame.MOUSEBUTTONDOWN :
                #get_pos can get the mouse cursor position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button,mouse_x,mouse_y):
    """when the palyer click the play_button , the game will start"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #Reset the game settings
        ai_settings.initialize_dynamic_settings()
        #hide cursor
        pygame.mouse.set_visible(False)
        #Resrt game statistics
        stats.reset_stats()
        stats.game_active = True
        #reset the Scoreboard image
        sb.preg_score()
        sb.preg_high_score()
        sb.preg_lever()
        sb.preg_ships()
        #empty alien's list and bullet's list
        aliens.empty()
        bullets.empty()
        #Establish a gruop of aliens  and leaves the ship in the middle
        create_many_alien(ai_settings,screen,ship,aliens)
        ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    screen.fill(ai_settings.bg_colour)  #fill the colour of screen
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()  #show the ship
    aliens.draw(screen) #显示alien  pygame自己绘制
    sb.show_score()# show the score information
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()  #make the recently drawn screen visble

def check_bullet_and_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    # check if the bullet shot down the alien ,if show down ,delete the bullet and alien
    # Collision detection is to check whether game elements overlap or not.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
           stats.score += ai_settings.alien_points * len(aliens)
           sb.preg_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        #delete the bullets ,speed up the game phythm and esrablish a group of aliens
        ai_settings.increase_speed()
        #Raise grade
        stats.lever +=1
        sb.preg_lever()
        create_many_alien(ai_settings, screen, ship, aliens)

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
     """updata bullet """
     bullets.update()
     # delete disappear bullets
     for bullet in bullets.copy():
         if bullet.rect.bottom <= 0:
             bullets.remove(bullet)
     check_bullet_and_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

"""alien"""
def get_number_alien_x(ai_settings,alien_width):
    """Calulate how many aliens in a row """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一个alien放在当前行'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    """Calulate how many rows of aliens the screen can hold"""
    available_space_y = (ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def create_many_alien(ai_settings,screen,ship,aliens):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    #calulate the number of aliens in a row
    number_aliens_x=get_number_alien_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #Establish a group of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    """when alien arrive  thr edges of screen, take relevant measures"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''take the all alien move down and change they direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *=-1

def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """Response to an alien crash into a ship"""
    if stats.ships_left > 0:
        stats.ships_left -=1
        #To update the Scoreboard
        sb.preg_    ships()
        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        #Restart
        create_many_alien(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #suspend
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """check if all alien  are at the edges of screen and update all alien's location"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #check the collision of the alien and the ship
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
    #check if the alien arrval the screen buttom
    check_alien_bottom(ai_settings, stats,sb, screen, ship, aliens, bullets)

def check_alien_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets):
    '''chack if aliens arrval the screen bottom'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
            break

def check_high_score(stats,sb):
    """check  dose it produce the highest score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.preg_high_score()