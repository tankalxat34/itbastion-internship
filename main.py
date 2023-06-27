"""
Главный файл приложения
"""

import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

import secrets
import string
import markdown
import markdownify

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def generate_alphanum_crypt_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(letters_and_digits) for i in range(length))
    print("Cryptic Random string of length", length, "is:", crypt_rand_string)
    return crypt_rand_string

app = Flask(__name__)
app.config['SECRET_KEY'] = generate_alphanum_crypt_string(256)


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("index.html", posts=posts)

@app.route('/post<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/delete<int:post_id>')
def delete(post_id):
    post = get_post(post_id)
    conn = get_db_connection()
    conn.execute("DELETE FROM posts WHERE id == ?", (post_id, ))
    conn.commit()
    conn.close()
    flash(f"Post '{post['title']}' with id {post['id']} has been deleted successfully!", "info")
    return redirect(url_for("index"))

@app.route('/create', methods=('GET', 'POST'))
def create():
    print(request.endpoint)
    if request.method == 'POST':
        title = request.form['title']
        content = (request.form['content'])

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                        (title, markdown.markdown(content)))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    markdown_content = markdownify.markdownify(post['content'] or request.form['content'])

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, markdown.markdown(content), id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post, markdown_content=markdown_content)

