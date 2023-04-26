from flask import Flask, render_template, request, redirect, url_for, flash, session, \
    send_from_directory, get_flashed_messages
from my_lib import database_worker, encrypt_password, check_password
from werkzeug.utils import secure_filename
from functools import wraps
import jwt
from datetime import datetime, timedelta
import dotenv
import os

app = Flask(__name__)
app.secret_key = 'you-will-never-guess'
app.config['UPLOAD_FOLDER'] = 'upload_folder'

dotenv.load_dotenv()
token_key = os.getenv('TOKEN_ENCRYPTION_KEY')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'token' not in session:
            print("No token")
            return redirect(url_for('login'))
        try:
            print("Decoding token")
            data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
        except:
            print("Wrong Token")
            return redirect(url_for('login'))

        return f(*args, **kwargs)

    return decorated

def create_database():
    db = database_worker("social_net.db")
    query_user = """CREATE table if not exists users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        country TEXT,
        username TEXT,
        email TEXT,
        password TEXT
    )
    """
    query_saves = """CREATE table if not exists saves(
        id INTEGER PRIMARY KEY,
        post_id INTEGER,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade,
        FOREIGN KEY (post_id) REFERENCES posts(id) on delete cascade
    )
    """
    query_comments = """CREATE table if not exists comments(
        id INTEGER PRIMARY KEY,
        timestamp TEXT,
        content TEXT,
        post_id INTEGER,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade,
        FOREIGN KEY (post_id) REFERENCES posts(id) on delete cascade
    )
    """
    query_follow = """CREATE table if not exists follow(
        id INTEGER PRIMARY KEY,
        follower INTEGER,
        followed INTEGER,
        FOREIGN KEY (follower) REFERENCES users(id) on delete cascade,
        FOREIGN KEY (followed) REFERENCES users(id) on delete cascade
    )
    """
    query_recipe = """CREATE table if not exists recipes(
        id INTEGER PRIMARY KEY,
        title VARCHAR(100),
        timestamp TEXT,
        content TEXT,
        ingredients TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
    )
    """
    query_restaurant = """CREATE table if not exists reviews(
        id INTEGER PRIMARY KEY,
        name VARCHAR(100),
        timestamp TEXT,
        stars INTEGER,
        content TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
    )
    """
    db.run_save(query_user)
    db.run_save(query_recipe)
    db.run_save(query_saves)
    db.run_save(query_comments)
    db.run_save(query_follow)
    db.run_save(query_restaurant)
    db.close()

@app.route('/')
@app.route('/index')
@token_required
def index():
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id = data['user_id']
    db = database_worker('social_net.db')
    query = f"SELECT * from users where id={user_id}"
    user = db.search(query=query)
    if user:
        id, name, surname, country, username, email, hash = user[0]
        user = {'username': name}
        return render_template('index.html', title='Home', user=user, login=True)
    return render_template('index.html', title='Home', login=True)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pswd']
        if len(email) > 0 and len(password) > 0:
            db = database_worker('social_net.db')
            login = f"SELECT * from users where email='{email}'"
            user = db.search(query=login)
            if user:
                id, name, surname, country, username, email, hash = user[0]
                if check_password(hashed_password=hash, user_password=password):
                    print("password is correct")
                    token = jwt.encode({'user_id': id, 'exp': datetime.utcnow() + timedelta(minutes=60)}, token_key, algorithm='HS256')
                    session['token'] = token
                    print("Token created.")
                    return redirect('/')
                else:
                    print("password is incorrect")
                    flash('Wrong password', 'danger')
            else:
                print("User does not exist.")
                flash('User does not exist', 'danger')
        else:
            print("Please fill in all fields.")
            flash('Please fill in all fields', 'danger')
    return render_template('login.html', title='Sign In', messages=get_flashed_messages())


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    db = database_worker("social_net.db")

    if request.method == "POST":
        name = request.form['name']
        surname = request.form['surname']
        username = request.form['username']
        country = request.form['country']
        email = request.form['email']
        password = request.form['passwd']
        password_confirm = request.form['passwd_check']
        if len(name) > 0 and len(username) > 0 and len(surname) and len(
                country) > 0 and len(email) > 0 and len(password) > 0:
            if password != password_confirm:
                print(password, password_confirm)
                flash(('Passwords do not match.', 'danger'))
                print("Passwords do not match.")
            elif len(password) < 8:
                flash(('Password must be at least 8 characters.', 'danger'))
                print("Password must be at least 8 characters.")

            else:
                register = f"INSERT into users(name, username, country, email, " \
                           f"password) values('{name}', '{username}', '{country}', " \
                           f"'{email}', '{encrypt_password(password)}')"
                db.run_save(query=register)
                flash(('Registration completed. Please log in.', 'success'))
                print("Registration completed. Please log in.")

                return redirect(url_for('login'))

    return render_template('signup.html', title='Sign up')

@app.route('/new-recipe', methods=['GET', 'POST'])
@token_required
def new_recipe():
    if request.method == 'POST':

    return render_template('new-recipe.html', title='New Recipe')

@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))

create_database()

if __name__ == '__main__':
    app.run()
