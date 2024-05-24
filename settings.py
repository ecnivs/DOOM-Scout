import math

# level 1-9
LEVEL = 1

# resolution
DOOM_RES = DOOM_W, DOOM_H = 320, 200
SCALE = 2.5
WIN_RES = WIDTH, HEIGHT = int(DOOM_W * SCALE), int(DOOM_H * SCALE)
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2

# field of view
FOV = 90.0
H_FOV = FOV / 2

# player settings
PLAYER_SPEED = 0.3
PLAYER_ROT_SPEED = 0.12
PLAYER_HEIGHT = 41

# screen settings
SCREEN_DIST = H_WIDTH / math.tan(math.radians(H_FOV))
COLOR_KEY = (152, 0, 136)
