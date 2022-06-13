from datetime import datetime, timedelta
from os import getenv
from utils.ResponseBuilder import ResponseBuilder 
from jwt import encode, decode
from jwt import exceptions

class AuthService:
    @staticmethod
    def write_token(data: dict):
        token = encode(payload={**data, "exp": AuthService.expire_date(2)}, 
                       key=getenv('SECRET'), algorithm = "HS256")
        return token
        
    @staticmethod
    def expire_date(days: int):
        now = datetime.now()
        expire = now + timedelta(days)

        return expire

    @staticmethod
    def validate_token(token, output = False):
        try:
            if output:
                return decode(token, key=getenv('SECRET'), algorithms = ["HS256"])
            decode(token, key=getenv('SECRET'), algorithms = ["HS256"])
        except exceptions.DecodeError:
            return ResponseBuilder.responseConfig(exceptions.DecodeError, 
                                                    {"message": "Invalid token", 
                                                    "status": 401})
        except exceptions.ExpiredSignatureError:
            return ResponseBuilder.responseConfig(exception = exceptions.ExpiredSignatureError, statusBody =
                                                    {"message": "Token Expired", 
                                                    "status": 401})
                                    