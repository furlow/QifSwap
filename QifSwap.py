import sys
import os
from PySide.QtCore import *
from PySide.QtGui import *

__appname__ = "Qifswap"

def swap_outflows_and_inflows(qif_filename):
    qif = open(qif_filename, 'r+')
    data = qif.read()
    data = data.replace('\nT','\nTemp')
    data = data.replace('\nTemp-','\nT')
    data = data.replace('\nTemp', '\nT-')
    qif.seek(0)
    qif.write(data)
    qif.close()

class Program(QDialog):
    def __init__(self, parent = None):
        super(Program, self).__init__(parent)
        self.setWindowTitle(__appname__)

        #Create button for opening credit card file
        self.open_file_button = QPushButton("Open File")

        #Align the widget in the container
        layout = QVBoxLayout()
        layout.addWidget(self.open_file_button)
        self.setLayout(layout)


        #connect to functions for saving
        self.open_file_button.clicked.connect(self.openQifFile)

    def openQifFile(self):
        qif_filename, _ = QFileDialog.getOpenFileName(self,
                                                    "Open File",
                                                    "",
                                                    "Bank File (*.qif)"
                                                    )
        if os.path.isfile(qif_filename):
            swap_outflows_and_inflows(qif_filename)


def main():
    sys.argv[0] = "QifSwap"
    app = QApplication(sys.argv)
    form = Program()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
