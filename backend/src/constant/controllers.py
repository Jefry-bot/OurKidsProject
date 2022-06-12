from controllers.ComplaintController import ComplaintController
from interceptors.ExceptionInterceptor import ExceptionInterceptor

complaint = ComplaintController()

CONTROLLERS = { "complaint": complaint }
