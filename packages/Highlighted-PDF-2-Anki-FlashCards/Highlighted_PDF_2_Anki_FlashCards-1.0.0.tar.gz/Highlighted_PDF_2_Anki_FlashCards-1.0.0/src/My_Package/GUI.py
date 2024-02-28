from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog
from PyQt6.QtCore import pyqtSlot
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton(self)
        btn.setText("Open file dialog")
        self.setCentralWidget(btn)
        btn.clicked.connect(self.open_dialog)
    
    def open_dialog(self):
        self.fname = QFileDialog.getOpenFileName(self,"Exportar relatório...", "" , "PDF (*.pdf);")
        print(self.fname)
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_gui = Main()
    main_gui.show()
    sys.exit(app.exec())