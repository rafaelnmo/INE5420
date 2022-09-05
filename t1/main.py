"""
Essa é uma aplicação que permite desenhar pontos, retas e polígonos. Além disso, ela também 
permite movimentar e dar zoom na viewport.

Autor: Rafael Oliveira e Andre Casagranda
Curso: INE5420 - Computacao Grafica
"""

import sys
#from Drawings  TODO
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QFrame, QSplitter, QApplication, QLabel)
from PyQt5.QtGui import QIcon

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

class MainWindow(QtWidgets.QMainWindow):
    """ This class defines the main window for the application."""
    def __init__(self):
        """Contructor for the MainWindow class (i.e. the entire application).
        
        :param self: represents a instance of the class MainWindow itself. Making possible to acces the attributes and methods of the class.
        :type self: class
        """
        super().__init__()
        self.objects = []       # list of tuples
        # Dict for the names of the buttons
        self.names = dict.fromkeys([0, 1, 2], ('Remove', 'Add'))
        self.names.update({3: ('-', '+')}) #
        self.InitUI()  # Instantiate the application components

    def InitUI(self):
        """This function instantiate all the components of the Application.

        :param self: represents a instance of the class MainWindow itself. Making possible to acces the attributes and methods of the class.
        :type self: class
        """
        # 1º Create the GroupBox
        groupBoxMenuFuncoes = QtWidgets.QGroupBox("Functions ")
        groupBoxMenuFuncoes.setFont(QtGui.QFont("Sanserif", 10))
        
        # 2º Create the BoxLayout
        vBoxMenuObjects = QtWidgets.QVBoxLayout()
        
        ### 3º Create the items ###
        self.listDrawElements = QtWidgets.QListWidget()
        self.labelDrawElements = QLabel("Objects Options")

        itemPonto = QtWidgets.QListWidgetItem("Point")
        self.listDrawElements.addItem(itemPonto)
        
        itemReta = QtWidgets.QListWidgetItem("Line")
        self.listDrawElements.addItem(itemReta)
        
        itemPoligono = QtWidgets.QListWidgetItem("Polygon")
        self.listDrawElements.addItem(itemPoligono)
        
        itemZoom = QtWidgets.QListWidgetItem("Zoom")
        self.listDrawElements.addItem(itemZoom)


        # Objects List
        self.listObjects = QtWidgets.QListWidget()
        self.labelObjects = QLabel("Objects List")
        # ----------------- #
        
        # 4º Add items to the Layout
        vBoxMenuObjects.addWidget(self.labelDrawElements)
        vBoxMenuObjects.addWidget(self.listDrawElements)
        vBoxMenuObjects.addWidget(self.labelObjects)
        vBoxMenuObjects.addWidget(self.listObjects)
        ### ---------------- ###

        # Creating Interactions
        self.groupBoxActions = QtWidgets.QGroupBox("Actions")
        vBoxMenuObjects.addWidget(self.groupBoxActions)

        # Auxiliar actions
        vBoxAuxiliarActions = QtWidgets.QHBoxLayout()
        
        self.minus = QtWidgets.QPushButton("-")
        self.plus = QtWidgets.QPushButton("+")
        
        vBoxAuxiliarActions.addWidget(self.minus)
        vBoxAuxiliarActions.addWidget(self.plus)
        self.groupBoxActions.setLayout(vBoxAuxiliarActions)
        
        self.label = QtWidgets.QLabel()
        vBoxMenuObjects.addWidget(self.label)
        
        groupBoxMenuFuncoes.setLayout(vBoxMenuObjects)
        
        ### Window ###
        #1° Create the GroupBox
        self.groupBoxWindow = QtWidgets.QGroupBox("Window")
        
        # 2° Create the layout
        vBoxWindow = QtWidgets.QVBoxLayout()

        # 3° Create the items
        self.up = QtWidgets.QPushButton("Up")
        self.right = QtWidgets.QPushButton("Right")
        self.down = QtWidgets.QPushButton("Down")
        self.left = QtWidgets.QPushButton("Left")
        
        # 4° Add the items to the layout
        vBoxWindow.addWidget(self.up)
        vBoxWindow.addWidget(self.right)
        vBoxWindow.addWidget(self.down)
        vBoxWindow.addWidget(self.left)
        
        # 5º Add the label
        self.label = QtWidgets.QLabel()
        vBoxMenuObjects.addWidget(self.label)
        
        # 6º Add the Layout to the GroupBox
        self.groupBoxWindow.setLayout(vBoxWindow)

        # 7º Add the GroupBox to the Parent Layout
        vBoxMenuObjects.addWidget(self.groupBoxWindow)

        ### ------------- ###

        ### Interactions ###
        debugTextBrowser = QtWidgets.QTextBrowser()
        self.canvas = Canvas()
        w = QtWidgets.QWidget()
        l = QtWidgets.QHBoxLayout()
        w.setLayout(l)
        # # dá zoom in na tela
        # zoomInButton.clicked.connect(self.canvas.on_zoom_in)
        # # dá zoom out na tela
        # zoomOutButton.clicked.connect(self.canvas.on_zoom_out)


        ### Left Box ###

        ### Left Part ###
        vertical = QtWidgets.QVBoxLayout()

        vertical.addWidget(self.canvas)
        vertical.addWidget(debugTextBrowser)
        ### Left Part ###

        l.addWidget(groupBoxMenuFuncoes)
        l.addLayout(vertical)
        w.setFixedSize(900, 700)

        self.setCentralWidget(w)
        self.show()


def main():
    """ Main function """
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
