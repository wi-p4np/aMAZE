
MAX_HEALTH = 3


class ScoreManager:
    score = 0
    gem_score = 0
    gameIsActive = True
    invincibilityTimer = 0
    isInvincible = False
    health = MAX_HEALTH
    pauseWindowIsActive = False
    deathWindowIsActive = False
    playerX = None
    playerY = None
