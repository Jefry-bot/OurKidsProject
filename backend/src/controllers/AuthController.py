import string
from flask import Blueprint, jsonify, request
from exceptions.NotFoundException import NotFoundException

from services.AuthService import AuthService

class AuthController:
    auth_routes: Blueprint = Blueprint("auth_routes", __name__)

    @auth_routes.post("/login")
    def login():
        data = request.get_json()

        if data['username'] == "Jefry":
            return AuthService.write_token(data = request.get_json())
        else: 
            raise NotFoundException("Not found data")

    @auth_routes.get("/verify/token")
    def verify():
        token = request.headers['Authorization'].split(" ")[1]
        return AuthService.validate_token(token, output = True)