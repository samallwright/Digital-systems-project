from distutils.log import debug
import sqlite3
from summarizer import summarizer
from flask import Flask, render_template, request, url_for, flash, redirect

# from flask_debug import Debug
from werkzeug.exceptions import abort

app = Flask(__name__)
# Debug(app)
# if __name__ == "__main__":
#     app.run(debug=True)
TEMPLATES_AUTO_RELOAD = True
app.config["SECRET_KEY"] = "your secret key"


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/about")
def about():
    return render_template("about.html")


@app.route(
    "/",
    methods=(
        "GET",
        "POST",
    ),
)
def index():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        query = request.form["query"]
        stigma = request.form["stigma"]
        prerequisite = int(request.form["preq_range"])
        size = int(request.form["size"])
        if not title:
            flash("Title is required!")
        if not content:
            flash("Text input is required!")
        if size == 0 and prerequisite == 0:
            flash("Choose EITHER quantity or %")
        else:
            summary, rouge_results, removed, reduction, speed = summarizer(
                title, content, query, stigma, prerequisite, size
            )
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO posts (title, content, summary, rouge, removed, reduction, speed) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (title, content, summary, rouge_results, removed, reduction, speed),
            )

            id = cursor.lastrowid
            conn.commit()
            conn.close()
            post = get_post(id)
            return render_template("post.html", post=post)
    return render_template("main_page.html")


@app.route("/posts")
def list_posts():
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return render_template("list_posts.html", posts=posts)


@app.route("/<int:post_id>")
def post(post_id):
    post = get_post(post_id)
    return render_template("post.html", post=post)


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
