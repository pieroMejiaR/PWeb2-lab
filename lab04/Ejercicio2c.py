from interpreter import draw
from chessPictures import *

white_queen = Picture(QUEEN)

board_queens = white_queen.join(white_queen).join(white_queen).join(white_queen)

draw(board_queens)