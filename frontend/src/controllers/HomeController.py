from PySide6.QtWidgets import QWidget
import requests
from screens.GeneralCustomUi import GeneralCustomUi
from screens.Login import Ui_Form

class Home(QWidget, Ui_Form):

    def __init__(self, session):
        super().__init__()
        self.setupUi(self)
        self.session = session
        self.ui = GeneralCustomUi(self)