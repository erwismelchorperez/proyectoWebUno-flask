from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    """
        flask --app app --debug run
    """
    # configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,#tiene el valor de True --> entorno de desarrollo, False --> entorno de producción
        SECRET_KEY = 'devapplication ',
        SQLALCHEMY_DATABASE_URI = "sqlite:///entidades.db"
    )
    
    db.init_app(app)

    #registrear blueprint
    from . import application
    app.register_blueprint(application.bp)

    #registrear blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template("index.html")
    
    with app.app_context():
        db.create_all()

    
    return app