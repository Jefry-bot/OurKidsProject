from PySide6.QtWidgets import QWidget
from screens.view import Ui_Form

class Home(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
