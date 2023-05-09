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
print(app.__class__.__name__)
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
        location TEXT,
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
    global posts, reviews
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id_title = data['user_id']
    db = database_worker('social_net.db')
    query = f"SELECT * from users where id={user_id_title}"
    user = db.search(query=query)
    if user:
        id, name, surname, country, username, email, hash = user[0]
        query_followed = f"SELECT followed from follow where follower={user_id_title}"
        followed = db.search(query=query_followed)
        followed = [i[0] for i in followed]
        followed = tuple(followed)
        for i in followed:
            query_posts = f"SELECT title, user_id, DATE(timestamp), content, id, user_id from recipes where user_id={i}"
            query_reviews = f"SELECT name, user_id, DATE(timestamp), content, id, user_id from reviews where user_id={i}"
            posts = db.search(query=query_posts)
            reviews = db.search(query=query_reviews)
            print(posts)
            for i in range(len(posts)):
                for j in range(len(posts[i])):
                    if j == 1:
                        posts = list(posts)
                        user_id = posts[i][j]
                        query_username = f"SELECT username from users where id={user_id}"
                        username = db.search(query=query_username)
                        posts[i] = list(posts[i])
                        posts[i][j] = username[0][0]

            for i in range(len(reviews)):
                for j in range(len(reviews[i])):
                    if j == 1:
                        reviews = list(reviews)
                        user_id = reviews[i][j]
                        query_username = f"SELECT username from users where id={user_id}"
                        username = db.search(query=query_username)
                        reviews[i] = list(reviews[i])
                        reviews[i][j] = username[0][0]
            print(posts)

        return render_template('index.html', title='Home', login=True, user_id=user_id_title, user=user, posts=posts, reviews=reviews)
    return render_template('index.html', title='Home', login=True, user_id=user_id_title, user=user)


@app.route('/explore', methods=['GET', 'POST'])
@token_required
def explore():
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id_title = data['user_id']
    db = database_worker('social_net.db')
    query = f"SELECT * from users where id={user_id_title}"
    user = db.search(query=query)
    if user:
        query_posts = f"SELECT title, user_id, DATE(timestamp), content, id, user_id from recipes"
        query_reviews = f"SELECT name, user_id, DATE(timestamp), content, id, user_id from reviews"
        posts = db.search(query=query_posts)
        reviews = db.search(query=query_reviews)
        for i in range(len(posts)):
            for j in range(len(posts[i])):
                if j == 1:
                    user_id = posts[i][j]
                    query_user = f"SELECT username from users where id={user_id}"
                    username = db.search(query=query_user)
                    posts[i] = list(posts[i])
                    posts[i][j] = username[0][0]
                    posts[i] = tuple(posts[i])
        for i in range(len(reviews)):
            for j in range(len(reviews[i])):
                if j == 1:
                    reviews = list(reviews)
                    user_id = reviews[i][j]
                    query_username = f"SELECT username from users where id={user_id}"
                    username = db.search(query=query_username)
                    reviews[i] = list(reviews[i])
                    reviews[i][j] = username[0][0]
        print(posts)
        return render_template('explore.html', title='Explore', user=user, posts=posts,
                               login=True, admin=user_id_title, reviews=reviews)
    return render_template('explore.html', title='follExplore', login=True,
                           admin=user_id_title)


@app.route('/delete_post/<int:post_id>')
@token_required
def delete_post(post_id):
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id_title = data['user_id']
    db = database_worker('social_net.db')
    query = f"SELECT * from users where id={user_id_title}"
    user = db.search(query=query)
    if user:
        query_post = f"DELETE from recipes where id={post_id}"
        db.run_save(query=query_post)
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/delete_review/<int:id>')
@token_required
def delete_review(id):
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id_title = data['user_id']
    db = database_worker('social_net.db')
    query = f"SELECT * from users where id={user_id_title}"
    user = db.search(query=query)
    if user:
        query_post = f"DELETE from reviews where id={id}"
        db.run_save(query=query_post)
        return redirect(url_for('profile_user'))
    return redirect(url_for('profile_user'))

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@token_required
def edit_post(post_id):
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id_title = data['user_id']
    db = database_worker('social_net.db')
    query = f"SELECT * from users where id={user_id_title}"
    user = db.search(query=query)
    if user:
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            ingredients = request.form['ingredients']
            query_post = f"UPDATE recipes set title='{title}', content='{content}', ingredients='{ingredients}' where id={post_id}"
            db.run_save(query=query_post)
            return redirect(url_for('index', user_id=user_id_title))
        query_post = f"SELECT title, content, ingredients, id from recipes where id={post_id}"
        post = db.search(query=query_post)
        return render_template('edit_post.html', title='Edit Post', user=user, post=post[0],
                               login=True, user_id=user_id_title)

@app.route('/edit_review/<int:id>', methods=['GET', 'POST'])
@token_required
def edit_review(id):
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id_title = data['user_id']
    db = database_worker('social_net.db')
    query = f"SELECT * from users where id={user_id_title}"
    user = db.search(query=query)
    if user:
        if request.method == 'POST':
            name = request.form['title']
            location = request.form['restaurant_address']
            content = request.form['content']
            rating = request.form['rating']
            query_post = f"UPDATE reviews set name='{name}', content='{content}', location='{location}', stars='{rating}' where id={id}"
            db.run_save(query=query_post)
            return redirect(url_for('profile_user', user_id=user_id_title))
        query_post = f"SELECT name, location, content, stars, id from reviews where id={id}"
        post = db.search(query=query_post)
        return render_template('edit_review.html', title='Edit Review', user=user, post=post[0],
                               login=True, user_id=user_id_title)


@app.route('/recipe/<int:post_id>')
@token_required
def recipe_page(post_id):
    global saved
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id_title = data['user_id']
    query = f"SELECT title, user_id, DATE(timestamp), content, ingredients, id, user_id from recipes where id={post_id}"
    db = database_worker('social_net.db')
    post = db.search(query=query)
    post_id = post[0][6]
    if post:
        user_id = post[0][1]
        query_user = f"SELECT username from users where id={user_id}"
        username = db.search(query=query_user)
        post = list(post[0])
        post[1] = username[0][0]
        post[6] = user_id
        post[4] = post[4].split(',')
        post = tuple(post)
        query_follow = f"SELECT * from follow where follower={user_id_title} and followed={post[6]}"
        follow = db.search(query=query_follow)
        if follow:
            follow = True
        else:
            follow = False
        query_saved = f"SELECT * from saves where user_id={user_id_title} and id={post_id}"
        saved = db.search(query=query_saved)
        if saved:
            saved = True
        else:
            saved = False
        return render_template('recipe-page.html', title=f'{post[0]}', post=post, login=True, user_id=user_id_title,
                               follow=follow, save=saved)
    return render_template('recipe-page.html', title=f'{post[0]}', login=True, user_id=user_id_title, save=saved)

@app.route('/review/<int:id>')
@token_required
def review(id):
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id_title = data['user_id']
    query = f"SELECT user_id, name, location, DATE(timestamp), content, stars, id, user_id from reviews where id={id}"
    db = database_worker('social_net.db')
    post = db.search(query=query)
    post_id = post[0][6]
    if post:
        user_id = post[0][0]
        query_user = f"SELECT username from users where id={user_id}"
        username = db.search(query=query_user)
        post = list(post[0])
        post[0] = username[0][0]
        post[6] = user_id
        post[4] = post[4].split(',')
        post = tuple(post)
        query_follow = f"SELECT * from follow where follower={user_id_title} and followed={post[6]}"
        follow = db.search(query=query_follow)
        if follow:
            follow = True
        else:
            follow = False
        return render_template('review.html', title=f'{post[0]}', post=post, login=True, user_id=user_id_title,
                                   follow=follow)
    return render_template('review.html', title=f'{post[0]}', login=True, user_id=user_id_title)


@app.route('/follow/<int:user_id>', methods=['GET', 'POST'])
@token_required
def follow(user_id):
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    follower = data['user_id']
    db = database_worker('social_net.db')
    query = f"SELECT * from users where id={follower}"
    user = db.search(query=query)
    if user:
        query_follow = f"INSERT INTO follow (follower, followed) VALUES ({follower}, {user_id})"
        db.run_save(query=query_follow)
        flash('You are now following this user', 'success')
        return redirect(url_for('profile', user_id=user_id))
    return redirect(url_for('profile', user_id=user_id))


@app.route('/unfollow/<int:user_id>', methods=['GET', 'POST'])
@token_required
def unfollow(user_id):
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    follower = data['user_id']
    db = database_worker('social_net.db')
    query = f"SELECT * from users where id={follower}"
    user = db.search(query=query)
    if user:
        query_follow = f"DELETE FROM follow WHERE follower={follower} and followed={user_id}"
        db.run_save(query=query_follow)
        flash('You are not following this user anymore', 'success')
        return redirect(url_for('profile', user_id=user_id))
        return redirect(url_for('profile', user_id=user_id))
    return redirect(url_for('profile', user_id=user_id))


@app.route('/saves')
@token_required
def saves():
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id_title = data['user_id']
    query = f"SELECT * from users where id={user_id_title}"
    db = database_worker('social_net.db')
    user = db.search(query=query)
    if user:
        query_saves = f"SELECT post_id from saves where user_id={user_id_title}"
        saves = db.search(query=query_saves)
        posts = []
        if saves:
            for i in range(len(saves)):
                query_posts = f"SELECT title, user_id, DATE(timestamp), content, id from recipes where id={saves[i][0]}"
                post = db.search(query=query_posts)
                for j in range(len(post)):
                    for k in range(len(post[j])):
                        if k == 1:
                            user_id = post[j][k]
                            query_user = f"SELECT username from users where id={user_id}"
                            username = db.search(query=query_user)
                            post[j] = list(post[j])
                            post[j][k] = username[0][0]
                            post[j] = tuple(post[j])
                posts.append(post[0])
            return render_template('saves.html', title='Saves', user=user, posts=posts,
                                   login=True, user_id=user_id_title)
        else:
            return render_template('saves.html', title='Saves', user=user, login=True, user_id=user_id_title,
                                   message="You don't have any saves yet.")
    return render_template('saves.html', title='Saves', login=True, user_id=user_id_title)


@app.route('/profile/<int:user_id>')
@token_required
def profile(user_id):
    query = f"SELECT * from users where id={user_id}"
    db = database_worker('social_net.db')
    user = db.search(query=query)
    if user:
        user = user[0]
        query_posts = f"SELECT title, user_id, DATE(timestamp), content, id from recipes where user_id={user_id}"
        posts = db.search(query=query_posts)
        for i in range(len(posts)):
            for j in range(len(posts[i])):
                if j == 1:
                    user_id = posts[i][j]
                    query_user = f"SELECT username from users where id={user_id}"
                    username = db.search(query=query_user)
                    posts[i] = list(posts[i])
                    posts[i][j] = username[0][0]
                    posts[i] = tuple(posts[i])
        # check if the active user follows the user whose profile is being viewed
        data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
        follower = data['user_id']
        query_follow = f"SELECT * from follow where follower={follower} and followed={user_id}"
        follow = db.search(query=query_follow)
        if follow:
            follow = True
        else:
            follow = False
        return render_template('profile.html', title=f'{user[0]}', user=user, posts=posts,
                               login=True, user_id=user_id, follow=follow)
    return render_template('profile.html', title=f'{user[0]}', login=True, user=user, user_id=user_id)


@app.route('/profile-user')
@token_required
def profile_user():
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id = data['user_id']
    query = f"SELECT * from users where id={user_id}"
    db = database_worker('social_net.db')
    user = db.search(query=query)
    if user:
        user = user[0]
        query_posts = f"SELECT title, user_id, DATE(timestamp), content, id from recipes where user_id={user_id}"
        query_reviews = f"SELECT name, user_id, DATE(timestamp), content, id, user_id from reviews where user_id={user_id}"
        posts = db.search(query=query_posts)
        reviews = db.search(query=query_reviews)
        for i in range(len(posts)):
            for j in range(len(posts[i])):
                if j == 1:
                    user_id = posts[i][j]
                    query_user = f"SELECT username from users where id={user_id}"
                    username = db.search(query=query_user)
                    posts[i] = list(posts[i])
                    posts[i][j] = username[0][0]
                    posts[i] = tuple(posts[i])
        for i in range(len(reviews)):
            for j in range(len(reviews[i])):
                if j == 1:
                    reviews = list(reviews)
                    user_id = reviews[i][j]
                    query_username = f"SELECT username from users where id={user_id}"
                    username = db.search(query=query_username)
                    reviews[i] = list(reviews[i])
                    reviews[i][j] = username[0][0]
        return render_template('profile-user.html', title=f'{user[0]}', user=user, posts=posts,
                               login=True, user_id=user_id, reviews=reviews)
    return render_template('profile-user.html', title=f'{user[0]}', login=True, user=user, user_id=user_id)


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
                    token = jwt.encode({'user_id': id, 'exp': datetime.utcnow() + timedelta(minutes=60)}, token_key,
                                       algorithm='HS256')
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
                flash('Passwords do not match.', 'danger')
                print("Passwords do not match.")
            elif len(password) < 8:
                flash('Password must be at least 8 characters.', 'danger')
                print("Password must be at least 8 characters.")

            else:
                register = f"INSERT into users(name, surname, username, country, email, " \
                           f"password) values('{name}', '{surname}', '{username}', '{country}', " \
                           f"'{email}', '{encrypt_password(password)}')"
                db.run_save(query=register)
                flash('Registration completed. Please log in.', 'success')
                print("Registration completed. Please log in.")

                return render_template('login.html', title='Sign In', messages=get_flashed_messages())
        else:
            flash('Please fill in all fields.', 'danger')
            print("Please fill in all fields.")

    return render_template('signup.html', title='Sign up', messages=get_flashed_messages())


@app.route('/new-recipe', methods=['GET', 'POST'])
@token_required
def new_recipe():
    global selected_ingredients, recipe_name
    ingredients_list = [
        'Flour',
        'Sugar',
        'Salt',
        'Pepper',
        'Eggs',
        'Milk',
        'Butter',
        'Baking powder',
        'Baking soda',
        'Yeast',
        'Vanilla extract',
        'Olive oil',
        'Vegetable oil',
        'Canola oil',
        'Honey',
        'Maple syrup',
        'Cornstarch',
        'Rice',
        'Pasta',
        'Bread crumbs',
        'Oats',
        'Chocolate chips',
        'Cocoa powder',
        'Nuts',
        'Seeds',
        'Cinnamon',
        'Nutmeg',
        'Cloves',
        'Ginger',
        'Garlic',
        'Onions',
        'Tomatoes',
        'Potatoes',
        'Carrots',
        'Celery',
        'Bell peppers',
        'Jalapenos',
        'Avocado',
        'Spinach',
        'Lettuce',
        'Cabbage',
        'Kale',
        'Broccoli',
        'Cauliflower',
        'Zucchini',
        'Eggplant',
        'Mushrooms',
        'Beef',
        'Chicken',
        'Pork',
        'Fish',
        'Shrimp',
        'Lobster',
        'Crab',
        'Scallops',
        'Soy sauce',
        'Vinegar',
        'Lemon juice',
        'Lime juice',
        'Worcestershire sauce',
        'Mustard',
        'Mayonnaise',
        'Ketchup',
        'Salsa',
        'Hot sauce',
        'Barbecue sauce',
        'Sour cream',
        'Cream cheese',
        'Cheddar cheese',
        'Parmesan cheese',
        'Mozzarella cheese',
        'Feta cheese',
        'Ricotta cheese',
        'Blue cheese',
        'Cottage cheese',
        'Cream',
        'Whipped cream',
        'Ice cream',
        'Yogurt',
        'Sour cream',
        'Hummus',
        'Tahini',
        'Peanut butter',
        'Jelly',
        'Jam',
        'Breadcrumbs',
        'Panko',
        'Almond flour',
        'Coconut flour',
        'Rye flour',
        'Cornmeal',
        'Graham crackers',
        'Marshmallows',
        'Gelatin'
    ]

    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id = data['user_id']
    if request.method == 'POST':
        print("In POST")
        recipe_name = request.form['recipe_name']
        selected_ingredients = request.form.getlist("ingredient")
        instructions = request.form['recipe_instructions']
        db = database_worker('social_net.db')
        query = f"SELECT * from users where id={user_id}"
        user = db.search(query=query)
        if user:
            print("User found.")
            query_new_recipe = f"INSERT into recipes(title, timestamp, content, " \
                               f"ingredients, user_id) values('{recipe_name}', " \
                               f"'{datetime.now()}', '{instructions}', " \
                               f"'{','.join(selected_ingredients)}', '{user_id}')"
            db.run_save(query=query_new_recipe)
            flash('Recipe added.', 'success')
            print("Recipe added.")
            return redirect(url_for('explore'))
        return render_template('index.html', messages=get_flashed_messages(), user=user, user_id=user_id, login=True)
    return render_template('new-recipe.html', title='New Recipe',
                           ingredients_list=ingredients_list, login=True, messages=get_flashed_messages(),
                           user_id=user_id)


@app.route('/new_review', methods=['GET', 'POST'])
@token_required
def new_review():
    print("In new_restaurant_review")
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id = data['user_id']
    if request.method == 'POST':
        print("In POST")
        restaurant_name = request.form['restaurant_name']
        location = request.form['restaurant_address']
        feedback = request.form['feedback']
        rate = request.form['rating']
        db = database_worker('social_net.db')
        query_new_review = f"INSERT into reviews(name, location, content, stars, user_id, timestamp) values('{restaurant_name}', '{location}', '{feedback}', '{rate}', '{user_id}', '{datetime.now()}' )"
        db.run_save(query=query_new_review)
        flash('Review added.', 'success')
        print("Review added.")
        return redirect(url_for('explore'))
    return render_template('new_review.html', title='New Restaurant Review',
                           login=True, messages=get_flashed_messages(),
                           user_id=user_id)


@app.route('/save_post', methods=['POST'])
@token_required
def save_post():
    post_id = request.form['post_id']
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id = data['user_id']
    db = database_worker('social_net.db')
    query = f"SELECT * from users where id={user_id}"
    user = db.search(query=query)
    if user:
        id, name, surname, country, username, email, hash = user[0]
        user = {'username': name}
        query_save = f"INSERT into saves(user_id, post_id) values('{user_id}', '{post_id}')"
        db.run_save(query=query_save)
        flash('Recipe saved.', 'success')
        print("Recipe saved.")
        return redirect(url_for('recipe_page', post_id=post_id, save=True, user=user, user_id=user_id))
    return render_template('index.html', messages=get_flashed_messages(), user=user, login=True, user_id=user_id)


@app.route('/unsave_post', methods=['POST'])
@token_required
def unsave_post():
    post_id = request.form['post_id']
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id = data['user_id']
    db = database_worker('social_net.db')
    query = f"SELECT * from users where id={user_id}"
    user = db.search(query=query)
    if user:
        query_unsave = f"DELETE from saves where user_id is {user_id} and post_id is {post_id}"
        db.run_save(query=query_unsave)
        flash('Recipe unsaved.', 'success')
        print("Recipe unsaved.")
        return redirect(url_for('recipe_page', post_id=post_id, save=False, user=user, user_id=user_id))
    return render_template('index.html', messages=get_flashed_messages(), user=user, login=True, user_id=user_id)


@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))


create_database()

if __name__ == '__main__':
    app.run(debug=True)
