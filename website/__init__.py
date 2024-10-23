from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    db_path = path.join(app.root_path, DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI']) 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Item
    
    create_database(app) 

    return app

def create_database(app):
    with app.app_context():
        if not path.exists(path.join(app.root_path, DB_NAME)):
            print("Creating database...")
            db.create_all()  
            print('Created Database!')
        else:
            print('Database already exists.')
