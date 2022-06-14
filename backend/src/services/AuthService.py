from datetime import datetime, timedelta
from os import getenv
from utils.ResponseBuilder import ResponseBuilder 
from jwt import encode, decode
from jwt import exceptions

class AuthService:
    @staticmethod
    def write_token(data: dict):
        token = encode(payload={**data, "exp": AuthService.expire_date(4)}, 
                       key=getenv('SECRET'), algorithm = "HS256")
        return token
        
    @staticmethod
    def expire_date(hours: int):
        now = datetime.now()
        expire = now + timedelta(hours = hours)

        return expire

    @staticmethod
    def validate_token(token, output = False):
        if output:
            return decode(token, key=getenv('SECRET'), algorithms = ["HS256"])
        decode(token, key=getenv('SECRET'), algorithms = ["HS256"])