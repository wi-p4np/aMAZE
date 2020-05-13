
MAX_HEALTH = 3


class ScoreManager:
    score = 0
    gem_score = 0
    game_is_active = True
    invincibility_timer = 0
    is_invincible = False
    health = MAX_HEALTH
    pause_window_is_active = False
    death_window_is_active = False
    start_game = False
    playerX = None
    playerY = None

