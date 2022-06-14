import string
from flask import Blueprint, jsonify, request
from exceptions.NotFoundException import NotFoundException

from services.AuthService import AuthService

class AuthController:
    auth_routes: Blueprint = Blueprint("auth_routes", __name__)

    @auth_routes.post("/login")
    def login():
        data = request.get_json()

        

    @auth_routes.get("/verify/token")
    def verify():
        token = request.headers['Authorization'].split(" ")[1]
        return AuthService.validate_token(token, output = True)