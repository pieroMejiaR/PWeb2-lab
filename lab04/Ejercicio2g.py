from interpreter import draw
from chessPictures import *

rock = Picture(ROCK)
knight = Picture(KNIGHT)
bishop = Picture(BISHOP)
queen = Picture(QUEEN)
white_space = Picture(SQUARE)
black_space = white_space.negative()

# Crear el tablero
board = white_space.join(black_space).horizontalRepeat(4)
board = board.under(black_space.join(white_space).horizontalRepeat(4)).verticalRepeat(4)

# Colocar las piezas en el tablero
board = board.overlay(rock.negative(), 0, 0)
board = board.overlay(knight.negative(), 0, len(SQUARE))
board = board.overlay(bishop.negative(), 0, len(SQUARE) * 2)
board = board.overlay(queen.negative(), 0, len(SQUARE) * 3)
board = board.overlay(king.negative(), 0, len(SQUARE) * 4)
board = board.overlay(bishop.negative(), 0, len(SQUARE) * 5)
board = board.overlay(knight.negative(), 0, len(SQUARE) * 6)
board = board.overlay(rock.negative(), 0, len(SQUARE) * 7)
for i in range(0, 8):
    board = board.overlay(pawn.negative(), len(SQUARE), i * len(SQUARE))
for i in range(0, 8):
    board = board.overlay(pawn, 6 * len(SQUARE), i * len(SQUARE))
board = board.overlay(rock, 7 * len(SQUARE), 0 * len(SQUARE))
board = board.overlay(knight, 7 * len(SQUARE), 1 * len(SQUARE))
board = board.overlay(bishop, 7 * len(SQUARE), 2 * len(SQUARE))
board = board.overlay(queen, 7 * len(SQUARE), 3 * len(SQUARE))
board = board.overlay(king, 7 * len(SQUARE), 4 * len(SQUARE))
board = board.overlay(bishop, 7 * len(SQUARE), 5 * len(SQUARE))
board = board.overlay(knight, 7 * len(SQUARE), 6 * len(SQUARE))
board = board.overlay(rock, 7 * len(SQUARE), 7 * len(SQUARE))

# Dibujar el tablero
draw(board)