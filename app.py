from flask import Flask, render_template, request
from my_lib import database_worker, hash_password, check_password

app = Flask(__name__) # create an instance of the Flask class

def create_database():
    print("Creating the database")
    db = database_worker("social_net.db")
    query_user = f"""CREATE TABLE if not exists users(
                id INTEGER PRIMARY KEY,
                name text,
                surname text,
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
                FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
    )           
    """
    db.run_save(query_user)
    db.run_save(query_posts)
    db.close()

def create_test_user():
    print("Creating test users")
    db = database_worker("social_net.db")
    users = ["contact@sabuhiabbasov.tech", "alice.doe@company.com"]
    passwords = ["qwerty", "12345678"]
    posts = [[{"title": "I am Sabuhi", "content": "Sabu"}, {"title": "I am Sabu",
                                                            "content": "Sabuhi"}],
             [{"title":"I am Alice", "content":"Alice"}]]
    for i in range(len(users)):
        user = users[i]
        pwd = passwords[i]
        posts_user = posts[i]

        query = f"""INSERT into users(email, password) values("{user}", "{hash_password(
            pwd)}")"""
        db.run_save(query)

        for p in posts_user:
            query = f"""INSERT into posts(title, content, user_id) values("
                        {p["title"]}", "{p["content"]}",1)"""
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
            jpy = int(usd_value)*132.615294
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
create_test_user()

if __name__ == '__main__':
    app.run()
