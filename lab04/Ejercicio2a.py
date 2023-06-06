from chessPictures import *
from interpreter import draw
from pieces import *
from picture import *


white_knight = Picture(KNIGHT)
black_knight = white_knight.negative()

board_knights = white_knight.join(black_knight).up(black_knight.join(white_knight))

draw(board_knights)