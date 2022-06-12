from flask import make_response
from exceptions.NotFoundException import NotFoundException
from utils.ExceptionBuilder import ExceptionBuilder
from utils.ResponseBuilder import ResponseBuilder


class ExceptionInterceptor:
    def error(self, error: Exception):
        return ResponseBuilder.failed(ExceptionBuilder.build(error))

    def notFound(self, error: NotFoundException):
        return ResponseBuilder.failedNotFound(ExceptionBuilder.build(error))