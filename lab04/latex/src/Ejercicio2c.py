from interpreter import draw
from chessPictures import *

white_queen = Picture(QUEEN)

board_queens = white_queen.horizontalRepeat(4)

draw(board_queens)