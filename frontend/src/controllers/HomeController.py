from PySide6.QtWidgets import QWidget
from screens.GeneralCustomUi import GeneralCustomUi
from screens.View import Form

class Home(QWidget, Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        
        
