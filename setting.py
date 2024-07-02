class Settings:
    """A class to store all settings for the game."""
    def __init__(self):
        """Initialize the game's settings."""
        self.bg_color = (255, 255, 255)  # White color
        self.ship_speed_factor = 1  # Speed factor for the ship
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
