from PySide6.QtCore import Qt
from requests import request, session
import requests
from entities.User import User
from services.AuthService import AuthService

class GeneralCustomUi:
    def __init__(self, ui, session) -> None:
        self.ui = ui
        self.session = session
        self.actions()

    def actions(self):
        self.ui.submit.clicked.connect(self.login)

    def login(self):
        user = User(username = self.ui.input_username.text(), 
                    password = self.ui.input_password.text())
        token = AuthService.login(user.__dict__)

        self.session.headers = {'Authorization': "Bearer " + str(token)} 

        if AuthService.verifyLogin(self.session):
            self.ui.label_verify.setText("Login success")