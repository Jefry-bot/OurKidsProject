import sys

from PySide6.QtWidgets import QApplication

from controllers.HomeController import Home

from services.ComplaintService import ComplaintService

if __name__ == '__main__':
    app = QApplication()
    service = ComplaintService()
    
    print(service.findById(9).name)
    window = Home()
    window.show()

    sys.exit(app.exec())