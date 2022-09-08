from PyQt5.QtWidgets import (QDialog, QDialogButtonBox, QFormLayout, QLabel, QLineEdit)

class ImportObjectWindow(QDialog):
    def __init__(self, parent=None, obj="Objeto"):
        super().__init__()

        self.setWindowTitle("Incluir {0}".format(obj))
        self.nameLineEdit = QLineEdit()
        self.parent = parent

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(self.getInfo)
        buttonBox.rejected.connect(self.reject)

        # creating a form layout
        layout = QFormLayout()
  
        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("Nome do {0}: ".format(obj)), self.nameLineEdit)

        layout.addWidget(buttonBox)
        self.setLayout(layout)
    
    def getInfo(self):
  
        # printing the form information
        name = self.nameLineEdit.text()
        print("Object Name: {0}".format(name))
        self.parent.import_object(name)
  
        # closing the window
        self.accept()
