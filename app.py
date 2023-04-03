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
                FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
    )           
    """
    db.run_save(query_user)
    db.run_save(query_posts)
    db.close()


def new_user():
    print("Adding new user")
    db = database_worker("social_net.db")
    user = ["Sabuhi", "Abbasov", "sabuhiabs", "2024.sabuhi.abbasov@uwcisak.jp",
            "Abbasov12@4"]
    query = f"""INSERT into users(name, surname, username, email, password) values(
    "{user[0]}", "{user[1]}", "{user[2]}", "{user[3]}", "{hash_password(user[4])}")"""
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

if __name__ == '__main__':
    app.run()
