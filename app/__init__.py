from flask import Flask

app = Flask(__name__)

def create_app():
    with app.app_context():
        from . import routes
    return app
