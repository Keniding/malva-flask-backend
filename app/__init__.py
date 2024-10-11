from flask import Flask
from config.config import Config
from database.db import db
from app.routes.reserva_routes import reserva_bp
from .middlewares.ip_restrictor import ip_restrictor

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    ip_restrictor(app)
    
    app.register_blueprint(reserva_bp, url_prefix='/reservas')
    
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    
    return app
