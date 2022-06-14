from controllers.AuthController import AuthController
from controllers.ComplaintController import ComplaintController
from controllers.UserController import UserController
from interceptors.ExceptionInterceptor import ExceptionInterceptor

complaint = ComplaintController()
auth = AuthController()
user = UserController()

CONTROLLERS = { "complaint": complaint, "auth": auth, "user": user}
