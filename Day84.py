from flask import Flask, render_template_string, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, name TEXT, password TEXT)''')
    conn.commit()
    conn.close()

# Initialize the database when the app starts
init_db()

# HTML templates
login_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            font-size: 24px;
        }
        input {
            font-size: 20px;
            padding: 5px;
            margin: 5px 0;
            width: 300px;
        }
        button {
            font-size: 20px;
            padding: 5px 20px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <form method="post" action="{{ url_for('login') }}">
        <div>Username: <input type="text" name="username" required></div>
        <div>Password: <input type="password" name="password" required></div>
        <button type="submit">Log in</button>
    </form>
    <p><a href="{{ url_for('signup') }}">Sign up</a></p>
    {% if error %}
    <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

signup_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Sign Up</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            font-size: 24px;
        }
        input {
            font-size: 20px;
            padding: 5px;
            margin: 5px 0;
            width: 300px;
        }
        button {
            font-size: 20px;
            padding: 5px 20px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <form method="post" action="{{ url_for('signup') }}">
        <div>Username: <input type="text" name="username" required></div>
        <div>Name: <input type="text" name="name" required></div>
        <div>Password: <input type="password" name="password" required></div>
        <button type="submit">Sign up</button>
    </form>
    <p><a href="{{ url_for('login') }}">Log in</a></p>
    {% if error %}
    <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

welcome_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <h1>Hello {{ name }}</h1>
    <p><a href="{{ url_for('logout') }}">Logout</a></p>
</body>
</html>
"""

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            session['username'] = username
            session['name'] = user[1]
            return redirect(url_for('welcome'))
        error = 'Invalid username or password'
    
    return render_template_string(login_template, error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        
        # Check if username already exists
        c.execute('SELECT 1 FROM users WHERE username = ?', (username,))
        if c.fetchone():
            error = 'Username already exists'
        else:
            hashed_password = generate_password_hash(password)
            c.execute('INSERT INTO users (username, name, password) VALUES (?, ?, ?)',
                     (username, name, hashed_password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        
        conn.close()
    
    return render_template_string(signup_template, error=error)

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template_string(welcome_template, name=session['name'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('name', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()