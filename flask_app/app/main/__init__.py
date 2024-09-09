from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes

if __name__ == "__main__":
    app.run(debug=True, port=7000)