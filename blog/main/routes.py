from blog.main import bp
from flask import render_template

@bp.route('/')
def index():
<<<<<<< HEAD
    return render_template('index.html')
=======
    return render_template('about.html')
>>>>>>> 38c03637ebfc1001f2b98e64821cdabebc99a4de
