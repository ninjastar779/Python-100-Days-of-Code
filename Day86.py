from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

# Mock user database
users = {
    'user1': {'password': 'password1'},
    'user2': {'password': 'password2'}
}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"User('{self.id}')"

class BlogPost:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f"BlogPost('{self.title}', '{self.author}')"

# Mock blog posts
blog_posts = [
    BlogPost('Post 1', 'This is the content of post 1', 'Author 1'),
    BlogPost('Post 2', 'This is the content of post 2', 'Author 2'),
    BlogPost('Post 3', 'This is the content of post 3', 'Author 3')
]

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('blog_posts'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/blog_posts')
@login_required
def blog_posts():
    return render_template('blog_posts.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)