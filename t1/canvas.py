from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Canvas(QtWidgets.QLabel):
    """This class defines the drawing area."""

    def __init__(self):
        """Contructor for the Canvas class (i.e. the drawing area). Making possible to acces the attributes and methods of the class.

        :param self: represents a instance of the class Canvas itself
        :type self: class
        """
        super().__init__()
        pixmap = QtGui.QPixmap(1000, 1000)  # Paint device (canvas)
        pixmap.fill(Qt.black)             # Background color for the canvas
        self.setPixmap(pixmap)
        self.function = 0
        # self.function_map = {
        #     0: self.draw_point,
        #     1: self.draw_line,
        #     2: self.draw_polygon,
        # }

        self.last_point = None
        self.pen_color = QtGui.QColor('#000000')
        self.scale = 1
