from blog.post import bp
from blog.extensions import db, ckeditor
from flask import (render_template, redirect,
                   url_for, request)
from blog.models.post import Post

@bp.route('/blog')
def blog():
    post = Post.query.all()
    return (render_template('post/index.html', post=post))

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form.get('ckeditor')

        post = Post(title=title,
                    content=content)

        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post.blog'))   
    return(render_template('post/create_post.html'))
 
@bp.route('/blog:<string:title>')
def title(title):
    post = Post.query.filter_by(title=title).first()

    if post:
        return(render_template('post/post.html', post=post)) 