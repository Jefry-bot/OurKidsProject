
import requests

from entities.Complaint import Complaint
from utils.Converter import Converter

class ComplaintService:
    def __init__(self, session) -> None:
        self.__url = "http://localhost:4000/api/complaints"
        self.session = session

    def findById(self, id: int) -> Complaint:
        data = self.session.get(self.__url + '/{id}'.format(id=id)).json()['data']

        return Converter.complaint(data)

    def findAll(self) -> list:
        data = self.session.get(self.__url).json()['data']

        return Converter.complaints(data)

    def deleteById(self, id: int) -> None:
        message = self.session.delete(self.__url + '/{id}'.format(id=id)).json()['message']

        return message

    def save(self, complaint: Complaint) -> None:
        message = self.session.post(self.__url, json = complaint.__dict__).json()['message']

        return message