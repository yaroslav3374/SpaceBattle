class Settings():
# Класс для хранения всех настроек игры Space Battle.

    def __init__(self):
# 
        self.screen_width = 1200
        self.screen_height = 640
        self.bg_color = (255,255,255)


        self.ship_limit = 3


        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = 255, 192, 209
        self.bullets_allowed = 25


        self.fleet_drop_speed = 1

# Темп ускорения игры
        self.speedup_scale = 1.1
# Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = -1

# Подсчет очков
        self.alien_points = 50


        self.fleet_direction = 1

    def increase_speed(self):
# Увеличивает настройки скорости и стоимость пришельцев.
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points / self.score_scale)
