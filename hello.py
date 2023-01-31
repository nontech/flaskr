from flask import Flask
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'{username}\'s profile'

# Test
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))



@app.route('/hello')
def hello():
    return 'Hello, WOrld'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the idis an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# @app.route("/<name>")
# def hello(name):
    # return f"Hello, {escape(name)}!"
