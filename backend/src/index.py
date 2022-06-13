from flask import Flask
from configurations.Settings import config

app = Flask(__name__)

if __name__ == '__main__':
    config(app)

    app.run(debug=True, port=4000)