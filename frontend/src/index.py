from re import A
import sys

from PySide6.QtWidgets import QApplication
from requests import session

from controllers.HomeController import Home
from services.complaints import ComplaintService

if __name__ == '__main__':
    app = QApplication()
    
    window = Home()
    window.show()

    sys.exit(app.exec())