from interpreter import draw
from chessPictures import *

white_space = Picture(SQUARE)
black_space = white_space.negative()

board = white_space.join(black_space).horizontalRepeat(4).under(black_space.join(white_space).horizontalRepeat(4)).verticalRepeat(2)

draw(board)