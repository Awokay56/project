from flask import render_template
from blog.contact import bp

@bp.route('/contact')
def contact():
    return(render_template('contact/index.html'))