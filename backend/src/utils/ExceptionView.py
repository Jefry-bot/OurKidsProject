from distutils.log import error
import logging
from traceback import print_last

from dtos.exceptionBody import ExceptionBody

class ExceptionView:
    
    @staticmethod
    def build(exception: ExceptionBody):
        error("{")

        print("   Cause: " + str(exception.cause))
        print("   Context: " + str(exception.context))
        print("   Traceback: " + str(exception.traceback))
        print("   Classname: " + str(exception.clazz))

        error("}")