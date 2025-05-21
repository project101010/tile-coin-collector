# Defining tuples for some standard colors.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# GAME SETTINGS
# Background , Resolution and Title.
# We're using 16x16 tiles so width 800 equals 50 tiles.
WIDTH = 800
# Height of 592 equals 37 tiles. (592/16)
HEIGHT = 592
FPS = 60
TITLE = "Tile Based Game!"
BGCOLOR = DARKGREY
# Grid size.
TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE



# PLAYER SETTINGS
PLAYER_SPEED = 250 # In pixels per seconds
PLAYER_SPRITE_RIGHT = 'tile_0080.png'
PLAYER_SPRITE_LEFT = 'tile_0077.png'
PLAYER_SPRITE_UP = 'tile_0079.png'
PLAYER_SPRITE_DOWN = 'tile_0078.png'
