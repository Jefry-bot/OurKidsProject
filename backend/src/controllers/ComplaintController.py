import string
from flask import Blueprint, request
from services.AuthService import AuthService

from services.ComplaintService import ComplaintService
from utils.ResponseBuilder import ResponseBuilder

class ComplaintController:
    complaint_routes: Blueprint = Blueprint("complaint_routes", __name__)
    __url: string = "/complaints"

    def __init__(self) -> None:
        global service
        service = ComplaintService()

    @complaint_routes.before_request
    def verify_token_middleware():
        token = request.headers['Authorization'].split(" ")[1]
        AuthService.validate_token(token, output = False)

    @complaint_routes.get(__url + "/<id>")
    def findById(id):
        return ResponseBuilder.success(service.findById(id))

    @complaint_routes.get(__url)
    def findAll():
        return ResponseBuilder.success(service.findAll()) 

    @complaint_routes.delete(__url + "/<id>")
    def deleteById(id):
        return ResponseBuilder.voidSuccess(service.deleteById, id)

    @complaint_routes.post(__url)
    def save():
        return ResponseBuilder.voidSuccess(service.save, request)

    @complaint_routes.get(__url + "/proof")
    def proof():
        return ResponseBuilder.success("Hello")