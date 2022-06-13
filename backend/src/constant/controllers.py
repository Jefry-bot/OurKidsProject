from controllers.AuthController import AuthController
from controllers.ComplaintController import ComplaintController
from interceptors.ExceptionInterceptor import ExceptionInterceptor

complaint = ComplaintController()
auth = AuthController()

CONTROLLERS = { "complaint": complaint, "auth": auth}
