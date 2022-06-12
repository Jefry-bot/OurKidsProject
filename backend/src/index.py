from flask import Flask

from constant.controllers import CONTROLLERS
from constant.interceptors import INTERCEPTORS
from exceptions.NotFoundException import NotFoundException
from interceptors.ExceptionInterceptor import ExceptionInterceptor

app = Flask(__name__)
interceptor = ExceptionInterceptor()

if __name__ == '__main__':
    for k in CONTROLLERS.keys():
        eval("app.register_blueprint(CONTROLLERS.get(k)." + str(k) + "_routes, url_prefix='/api')")

    app.run(debug=True, port=4000)