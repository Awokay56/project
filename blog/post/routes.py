from blog.post import bp

from flask import render_template

@bp.route('/blog')
def blog():
    return (render_template(('post/index.html')))