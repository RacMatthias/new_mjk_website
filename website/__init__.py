from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mjk_app_database.sqlite3'
 
    db.init_app(app)

    with app.app_context():
        from .views import views
        from .api import api

        db.create_all()

    app.register_blueprint(views)
    app.register_blueprint(api)

    return app