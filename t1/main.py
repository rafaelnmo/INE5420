"""
Essa é uma aplicação que permite desenhar pontos, retas e polígonos. Além disso, ela também 
permite movimentar e dar zoom na viewport.

Autor: Rafael Oliveira e Andre Casagranda
Curso: INE5420 - Computacao Grafica
"""

import sys
# from Drawings  TODO
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QFrame, QSplitter, QApplication, QLabel)
from PyQt5.QtGui import QIcon

from main_window import MainWindow


def main():
    """ Main function """
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
