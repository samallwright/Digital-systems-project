import sqlite3
from turtle import pos
import stop_word
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True
app.config['SECRET_KEY'] = 'your secret key'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=('GET','POST',))
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        if not content:
            flash('Text input is required!')
        else:
            summary = stop_word.stop_word_vomit(content)
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content, summary) VALUES (?, ?, ?)', 
                         (title, content, summary))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    return render_template('main_page.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post