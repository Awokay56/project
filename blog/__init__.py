from flask import Flask
from config import Config
from blog.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize flask extensions
    db.init_app(app)

    # Registering blueprints
    from blog.main import bp as main_bp
    app.register_blueprint(main_bp)


    return app