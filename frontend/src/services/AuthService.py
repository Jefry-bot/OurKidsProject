
import requests
from entities.Complaint import Complaint

class AuthService:
    global __url
    __url = "http://localhost:4000/api/login"     

    @staticmethod
    def login(data: dict) -> Complaint:
        token = requests.Session().post(__url, json = data).text
        return token

    @staticmethod
    def verifyLogin(session):
        if session.headers['Authorization'].split(" ")[1][0] == "{":
            raise Exception()

        data = session.get("http://localhost:4000/api/verify/token").json()['exp']
        
        if data:
            return True
        return False