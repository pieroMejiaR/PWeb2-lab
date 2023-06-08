from colors import *

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return Picture(vertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        horizontal = self.img[::-1]
        return Picture(horizontal)

    def negative(self):
        # Crear una lista vacía para almacenar las líneas de la imagen negativa
        negative_img = []

        # Iterar sobre las líneas de la imagen actual
        for line in self.img:
            # Reemplazar el color de cada carácter en la línea
            inverted_line = [self._invColor(c) for c in line]
            # Agregar la línea modificada a la lista de la imagen negativa
            negative_img.append("".join(inverted_line))

        # Crear y retornar una nueva instancia de Picture con la imagen negativa
        return Picture(negative_img)
    
    def join(self, p):
        joined = []
        for i in range(len(self.img)):
            joined.append(self.img[i] + p.img[i])
        return Picture(joined)

    def up(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        return Picture(p.img + self.img)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p debajo de la
            figura actual """
        return Picture(self.img + p.img)

    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        repeated = []
        for row in self.img:
            repeated_row = ''
            for _ in range(n):
                repeated_row += row
            repeated.append(repeated_row)
        return Picture(repeated)

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual verticalmente
            la cantidad de veces que indique el valor de n """
        repeated = []
        for _ in range(n):
            repeated.extend(self.img)
        return Picture(repeated)

    def rotate(self):
        """ Devuelve una figura rotada en 90 grados en sentido horario """
        rotated = []
        for i in range(len(self.img[0])):
            rotated_row = ''
            for j in range(len(self.img) - 1, -1, -1):
                rotated_row += self.img[j][i]
            rotated.append(rotated_row)
        return Picture(rotated)
    
    def overlay(self, piece, row, col):
        new_img = self.img.copy()
        piece_img = piece.img

        piece_height = len(piece_img)
        piece_width = len(piece_img[0])

        for i in range(piece_height):
            for j in range(piece_width):
                if piece_img[i][j] != ' ':
                    new_row = row + i
                    new_col = col + j
                    new_img[new_row] = new_img[new_row][:new_col] + piece_img[i][j] + new_img[new_row][new_col + 1:]

        return Picture(new_img)