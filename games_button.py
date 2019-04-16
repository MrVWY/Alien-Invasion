import pygame.font
"""pygame.font ability to render text to the screen"""

class Button():
    #msg is a include words file
    def __init__(self,ai_settings,screen,msg):
        """Initilization button properties"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #set button size and other attributes
        self.width,self.height = 200,50
        self.button_colour = (0,255,0)
        self.text_colour = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #Establish the button's rect , make it centered
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #The button's label only creat once
        self.preg_msg(msg)

    def preg_msg(self,msg):
        """make the msg to image , let its location is in the center and upper """
        self.msg_image = self.font.render(msg,True,self.text_colour,self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #make a colour to fill the button and draw the text
        self.screen.fill(self.button_colour,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)