from flask import Flask, render_template, request
from my_lib import database_worker, hash_password, check_password

app = Flask(__name__)  # create an instance of the Flask class


def create_database():
    print("Creating the database")
    db = database_worker("social_net.db")
    query_user = f"""CREATE TABLE if not exists users(
                id INTEGER PRIMARY KEY,
                name text,
                surname text,
                country text,
                username text unique,
                email text unique,
                password text
    )
    """
    query_posts = f"""CREATE TABLE if not exists posts(
                id INTEGER PRIMARY KEY,
                title VARCHAR(150),
                content text,
                user_id INTEGER,
                category text,
                created_at text,
                FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
    )           
    """
    query_comments = f"""CREATE TABLE if not exists comments(
                id INTEGER PRIMARY KEY,
                post_id INTEGER,
                user_id,
                created_at text,
                comment text,
                FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade,
                FOREIGN KEY (post_id) REFERENCES posts(id) on delete cascade
    )           
    """
    db.run_save(query_user)
    db.run_save(query_posts)
    db.run_save(query_comments)
    db.close()


def new_user():
    print("Adding new user")
    db = database_worker("social_net.db")
    user = ["Eva", "Chen", "evachen88", "Canada", "eva.chen88@gmail.com", "ilovecoding!"]
    query = f"""INSERT into users(name, surname, username, country, email, password) 
    values("{user[0]}", "{user[1]}", "{user[2]}", "{user[3]}", "{user[4]}", "{hash_password(user[4])}")"""
    db.run_save(query)
def new_post():
    print("Adding new post")
    db = database_worker("social_net.db")
    posts = ["Kiku Japanese Restaurant", """Kiku Japanese Restaurant is a must-visit for anyone who loves authentic Japanese cuisine. Located in the heart of Tokyo, this restaurant is a hidden gem that offers some of the best sushi, tempura, and sake in the city.
I recently visited Kiku Japanese Restaurant with some friends, and we were blown away by the quality of the food and the friendly service. We started with the Tokyo Garden Salad, which was a refreshing mix of crispy iceberg lettuce, crispy wonton strips, pickled ginger, and sesame seeds. The dressing was perfectly balanced and brought out the flavors of the ingredients.
For our main course, we ordered a variety of sushi rolls and tempura dishes. The sushi was some of the freshest and most flavorful I've ever tasted, and the tempura was perfectly crispy and not greasy at all. We also tried a few different types of sake, which were all excellent
The ambiance of the restaurant was also very nice, with traditional Japanese decor and a cozy atmosphere. The staff were very attentive and made us feel welcome throughout the meal.
Overall, I would highly recommend Kiku Japanese Restaurant to anyone who is looking for an authentic Japanese dining experience in Tokyo. The quality of the food and service is truly outstanding, and I can't wait to visit again next time I'm in town!""", "Restaurant Reviews", "04/03/2023", 3]

    query =f"""INSERT into posts(title, content, category, created_at, user_id) VALUES("
    {posts[0]}", "{posts[1]}", "{posts[2]}", "{posts[3]}", "{posts[4]}" )"""
    db.run_save(query)

def new_comment():
    print("Adding new comment")
    db = database_worker("social_net.db")
    comment = [3, 4, "04/04/2023 12:30:15", "I'm definitely trying this recipe tonight!"]

    query = f""""""
    db.run_save(query)


@app.route('/home')
def home():
    return 'This is my home page'


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/requests_example', methods=["GET", "POST"])
def requests_example():
    result = ""
    result2 = ""
    if request.method == "GET":
        # currency converter
        usd_value = request.args.get("usd_value")
        if usd_value:
            jpy = int(usd_value) * 132.615294
            result = f"{usd_value} USD is {jpy:.2f} JPY"
    elif request.method == "POST":
        # password checker
        check_pass = request.form["check_pass"]
        if check_pass:
            if len(check_pass) > 8:
                result2 = "Strong password"
            else:
                result2 = "Unsafe password"
    return render_template('requests_example.html', data=result, data2=result2)


create_database()
# new_user()
# new_post()
new_comment()

if __name__ == '__main__':
    app.run()
