from interpreter import draw
from chessPictures import *

white_knight = Picture(KNIGHT)
black_knight = white_knight.negative()

board_knights = white_knight.join(black_knight).up(black_knight.verticalMirror().join(white_knight.verticalMirror()))

draw(board_knights)