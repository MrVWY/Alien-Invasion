class status():
    """Track game statistics"""
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        """when the game start ,Being active"""
        self.game_active = False
        # In any case , the high_score shouldn't reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics for possible changes in the game"""
        self.ships_left =self.ai_settings.ship_limit
        self.score = 0
        self.lever = 1


