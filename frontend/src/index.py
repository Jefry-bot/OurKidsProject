import sys

from PySide6.QtWidgets import QApplication

from controllers.HomeController import Home

if __name__ == '__main__':
    app = QApplication()
    
    window = Home()
    window.show()

    sys.exit(app.exec())