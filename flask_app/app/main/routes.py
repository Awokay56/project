from flask import render_template
from app.main import bp


@bp.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    bp.run(debug=True, port=5001)