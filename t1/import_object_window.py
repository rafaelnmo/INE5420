from PyQt5.QtWidgets import (QDialog, QDialogButtonBox, QFormLayout, QLabel, QLineEdit, QHBoxLayout, QSpinBox)

from graphic_objects import Point, Wireframe

class ImportObjectWindow(QDialog):
    def __init__(self, parent=None, obj="Objeto"):
        super().__init__()

        self.setWindowTitle("Incluir {0}".format(obj))
        self.nameEdit = QLineEdit()
        self.x1Edit = QSpinBox()
        self.y1Edit = QSpinBox()
        self.parent = parent

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(self.getInfo)
        buttonBox.rejected.connect(self.reject)

        # creating a form layout
        layout = QFormLayout()
  
        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("Nome do {0}: ".format(obj)), self.nameEdit)

        hLayout = QHBoxLayout()
        hLayout.addWidget(QLabel("X:"))
        hLayout.addWidget(self.x1Edit)
        hLayout.addWidget(QLabel("Y:"))
        hLayout.addWidget(self.y1Edit)

        layout.addRow(hLayout)

        layout.addWidget(buttonBox)
        self.setLayout(layout)
    
    def getInfo(self):
  
        # printing the form information
        name = self.nameEdit.text()
        x = self.x1Edit.text()
        y = self.y1Edit.text()

        obj = Wireframe(name, [Point("", int(x), int(y)), Point("", int(y)+10, int(x)+10)])

        print("Object Name: {0}".format(obj.name))
        print("Object X1: {0}".format(obj.points[0].x))
        print("Object Y1: {0}".format(obj.points[0].y))
        print("Object X2: {0}".format(obj.points[1].x))
        print("Object Y2: {0}".format(obj.points[1].y))
        self.parent.import_object(obj)
  
        # closing the window
        self.accept()
