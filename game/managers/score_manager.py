
MAX_HEALTH = 3


class ScoreManager:
    score = 0
    gameIsActive = True
    invincibilityTimer = 0
    isInvincible = False
    health = MAX_HEALTH
    pauseWindowIsActive = False
    playerX = None
    playerY = None
