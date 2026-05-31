from app.controller.controller import controller
from flask import Flask

def createApp():
    app = Flask(__name__, template_folder='view')
    app.register_blueprint(controller)
    return app