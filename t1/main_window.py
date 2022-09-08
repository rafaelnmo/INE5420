from PyQt5 import QtGui
from PyQt5.QtWidgets import (QMainWindow, QGroupBox, QListWidget, QVBoxLayout, QListWidgetItem, QLabel, QHBoxLayout, QPushButton, QTextBrowser, QWidget)

from import_object_window import ImportObjectWindow

from canvas import Canvas

class MainWindow(QMainWindow):
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
        self.names.update({3: ('-', '+')})
        self.InitUI()  # Instantiate the application components

    def InitUI(self):
        """This function instantiate all the components of the Application.

        :param self: represents a instance of the class MainWindow itself. Making possible to acces the attributes and methods of the class.
        :type self: class
        """
        # 1º Create the GroupBox
        groupBoxMenuFuncoes = QGroupBox("Functions ")
        groupBoxMenuFuncoes.setFont(QtGui.QFont("Sanserif", 10))

        # 2º Create the BoxLayout
        vBoxMenuObjects = QVBoxLayout()

        ### 3º Create the items ###
        self.listDrawElements = QListWidget()
        self.labelDrawElements = QLabel("Objects Options")

        itemPonto = QListWidgetItem("Point")
        self.listDrawElements.addItem(itemPonto)

        itemReta = QListWidgetItem("Line")
        self.listDrawElements.addItem(itemReta)

        itemPoligono = QListWidgetItem("Polygon")
        self.listDrawElements.addItem(itemPoligono)

        itemZoom = QListWidgetItem("Zoom")
        self.listDrawElements.addItem(itemZoom)
        # Call the function to process a click
        self.listDrawElements.clicked.connect(self.listview_clicked)
        self.listDrawElements.setCurrentItem(itemZoom)

        # Objects List
        self.listObjects = QListWidget()
        self.labelObjects = QLabel("Objects List")
        # ----------------- #

        # 4º Add items to the Layout
        vBoxMenuObjects.addWidget(self.labelDrawElements)
        vBoxMenuObjects.addWidget(self.listDrawElements)
        vBoxMenuObjects.addWidget(self.labelObjects)
        vBoxMenuObjects.addWidget(self.listObjects)
        ### ---------------- ###

        # Creating Interactions
        self.groupBoxActions = QGroupBox("Actions")
        vBoxMenuObjects.addWidget(self.groupBoxActions)

        # Auxiliar actions
        vBoxAuxiliarActions = QHBoxLayout()

        self.buttonAux1 = QPushButton("-")
        self.buttonAux2 = QPushButton("+")
        self.buttonAux2.clicked.connect(self.open_import_window)

        vBoxAuxiliarActions.addWidget(self.buttonAux1)
        vBoxAuxiliarActions.addWidget(self.buttonAux2)
        self.groupBoxActions.setLayout(vBoxAuxiliarActions)

        self.label = QLabel()
        vBoxMenuObjects.addWidget(self.label)

        groupBoxMenuFuncoes.setLayout(vBoxMenuObjects)

        ### Window ###
        # 1° Create the GroupBox
        self.groupBoxWindow = QGroupBox("Window")

        # 2° Create the layout
        vBoxWindow = QVBoxLayout()

        # 3° Create the items
        self.up = QPushButton("Up")
        self.right = QPushButton("Right")
        self.down = QPushButton("Down")
        self.left = QPushButton("Left")

        # 4° Add the items to the layout
        vBoxWindow.addWidget(self.up)
        vBoxWindow.addWidget(self.right)
        vBoxWindow.addWidget(self.down)
        vBoxWindow.addWidget(self.left)

        # 5º Add the label to the GroupBox
        self.label = QLabel()
        vBoxMenuObjects.addWidget(self.label)

        # 6º Add the Layout to the GroupBox
        self.groupBoxWindow.setLayout(vBoxWindow)

        # 7º Add the GroupBox to the Parent Layout
        vBoxMenuObjects.addWidget(self.groupBoxWindow)

        # 2° Create the layout
        vBoxZoom = QHBoxLayout()

        # 3° Create the items
        self.minus = QPushButton("+")
        self.plus = QPushButton("-")

        # 4° Add the items to the layout
        vBoxZoom.addWidget(self.minus)
        vBoxZoom.addWidget(self.plus)

        # 5º Add the label to the GroupBox
        self.label = QLabel()
        vBoxMenuObjects.addWidget(self.label)

        # 6º Add the Layout to the GroupBox
        self.groupBoxWindow.setLayout(vBoxZoom)
        ### ------------- ###

        ### Interactions ###
        debugTextBrowser = QTextBrowser()
        self.canvas = Canvas()
        w = QWidget()
        l = QHBoxLayout()
        w.setLayout(l)
        # # dá zoom in na tela
        # zoomInButton.clicked.connect(self.canvas.on_zoom_in)
        # # dá zoom out na tela
        # zoomOutButton.clicked.connect(self.canvas.on_zoom_out)

        ### Left Box ###

        ### Left Part ###
        vertical = QVBoxLayout()

        vertical.addWidget(self.canvas)
        vertical.addWidget(debugTextBrowser)
        ### Left Part ###

        l.addWidget(groupBoxMenuFuncoes)
        l.addLayout(vertical)
        w.setFixedSize(900, 900)

        self.setCentralWidget(w)
        self.show()

    def listview_clicked(self):
        """This function handle click on the buttons.

        :param self: represents a instance of the class MainWindow itself. Making possible to acces the attributes and methods of the class.
        :type self: class
        """
        text = self.listDrawElements.selectedItems()[0].text()
        self.groupBoxActions.setTitle(text)

        item = self.listDrawElements.currentRow()
        print(item)
        l, r = self.names[item]
        print((l, r))
        self.buttonAux1.setText(l)
        self.buttonAux2.setText(r)

        # self.canvas.set_funciont(item)
        # print(item)
        self.label.setText('Item : ' + str(item + 1))

    def open_import_window(self):
        """TODO: This function instantiate objects on the screen.

        :param self: represents a instance of the class MainWindow itself. Making possible to acces the attributes and methods of the class.
        :type self: class

        """

        obj = self.listDrawElements.selectedItems()[0].text()
        print("Adding item:", obj)

        dlg = ImportObjectWindow(self, obj)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

        self.update()

    def import_object(self, name):
        print("Importing object:", name)