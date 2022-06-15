
import requests

from entities.Complaint import Complaint
from entities.User import User
from utils.Converter import Converter

class UserService:
    def __init__(self) -> None:
        self.__url = "http://localhost:4000/api/users"
        self.session = requests.Session()

    def findById(self, id: int) -> User:
        data = self.session.get(self.__url + '/{id}'.format(id=id)).json()['data']

        return Converter.user(data)

    def findAll(self) -> list:
        data = self.session.get(self.__url).json()['data']

        return Converter.users(data)

    def deleteById(self, id: int) -> None:
        message = self.session.delete(self.__url + '/{id}'.format(id=id)).json()['message']

        return message

    def save(self, user: User) -> None:
        message = self.session.post(self.__url, json = user.__dict__).json()['message']

        return message