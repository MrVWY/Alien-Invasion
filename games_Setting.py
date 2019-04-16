class  Setting():
    """存储外星人入侵的所有设置类"""
    def __init__(self):
        self.screen_width=1200
        self.screen_height =800
        self.bg_colour = (230,230,230)

        #ship settins
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #set up the bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60,60,60)
        self.bullet_allowed = 3 #limit bullet number

        #alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        #1 expression move right ,-1 expression move left
        self.fleet_direction = 1

        #How to Speed the game phythm
        self.speedup_scale = 1.1
        #aliens's point speed up
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change as the game progresses"""
        self.alien_speed_factor = 2
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3

        # 1 expression move right ,-1 expression move left
        self.fleet_direction = 1
        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Speed up  , aliens's point"""
        self.alien_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

