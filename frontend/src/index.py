import sys

from PySide6.QtWidgets import QApplication
import requests

from controllers.HomeController import Home

if __name__ == '__main__':
    app = QApplication()
    session = requests.Session()
    
    window = Home(session)
    session = window.session
    window.show()

    sys.exit(app.exec())