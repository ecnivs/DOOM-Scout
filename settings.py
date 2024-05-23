import math

# DOOM resolution
DOOM_RES = DOOM_W, DOOM_H = 320, 200

SCALE = 5.0
WIN_RES = WIDTH, HEIGHT = int(DOOM_W * SCALE), int(DOOM_H * SCALE)
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2

# field of view
FOV = 90.0
H_FOV = FOV / 2

# player
PLAYER_SPEED = 0.3
PLAYER_ROT_SPEED = 0.12
