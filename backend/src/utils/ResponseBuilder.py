
from flask import jsonify, make_response
from dtos.response import Response
from utils.ExceptionView import ExceptionView


class ResponseBuilder:
    @staticmethod
    def success(object: object) -> Response:
        if object.__class__.__name__ != 'list':
            object = object.__dict__

        response = Response(
            data = object,
            message = "Proccess to success in server",
            status = 200
        )
        
        return jsonify(response.__dict__)

    @staticmethod
    def voidSuccess(func, object: object = None) -> Response:
        if object == None:
            func()
        else:
            func(object)

        response = Response(
            data = None,
            message = "Proccess to success in server",
            status = 200
        )
        
        return jsonify(response.__dict__)

    @staticmethod
    def failed(exception) -> Response:
        ExceptionView.build(exception)

        response = Response(
            data = None,
            message = "An error has occurred on the server",
            status = 500
        )
        
        return make_response(jsonify(response.__dict__), 500)

    @staticmethod
    def failedNotFound(exception) -> Response:
        ExceptionView.build(exception)

        response = Response(
            data = None,
            message = "Not found data in server",
            status = 404
        )
        
        return make_response(jsonify(response.__dict__), 404)
        