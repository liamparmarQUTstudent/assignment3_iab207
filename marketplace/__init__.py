from flask import Flask 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()

def create_app():
    #print(__name__)
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///items.sqlite'
    db.init_app(app)
    app.secret_key='hi'

    bootstrap = Bootstrap(app)

    login_manager = LoginManager()
    login_manager.login_view ='auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from . import views
    app.register_blueprint(views.mainbp)

    from . import ItemDetails
    app.register_blueprint(ItemDetails.bp)
 
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app
