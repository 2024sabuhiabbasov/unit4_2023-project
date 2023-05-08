# Foodie: A Social Network for Food Lovers
<img src="https://user-images.githubusercontent.com/111758436/229414078-7b5067ff-7633-4fb9-9ec2-4d1091d0e5e3.png" style="width:100%">
<p align="center">
  Using the prompt 'Generate a picture of a cozy kitchen with ingredients and utensils for cooking a delicious meal in a rustic and warm colors,' this image was generated using AI on Deep Dream Generator.[1]
</p>

<!-- TOC -->
* [Foodie: A Social Network for Food Lovers](#foodie-a-social-network-for-food-lovers)
* [Criteria A: Planning](#criteria-a-planning)
  * [Problem Definition](#problem-definition)
  * [Proposed Solution](#proposed-solution)
    * [Design Statement](#design-statement)
    * [Rationale for Proposed Solution](#rationale-for-proposed-solution)
    * [Success Criteria](#success-criteria)
* [Criteria B: Design](#criteria-b-design)
  * [System Diagram](#system-diagram)
  * [Wireframe](#wireframe)
  * [Flow Diagram](#flow-diagram)
    * [Flow Diagram 1 - Follow Feature](#flow-diagram-1---follow-feature)
    * [Flow Diagram 2 - Login Feature](#flow-diagram-2---login-feature)
    * [Flow Diagram 3 - New Review Feature](#flow-diagram-3---new-review-feature)
  * [ER Diagram](#er-diagram)
  * [UML Diagram](#uml-diagram)
  * [Test plan](#test-plan)
  * [Record of Tasks](#record-of-tasks)
* [Criteria C: Development](#criteria-c-development)
  * [Existing tools](#existing-tools)
  * [List of techniques used](#list-of-techniques-used)
  * [Development](#development)
* [Criteria D: Functionality](#criteria-d-functionality)
  * [A video demonstrating the proposed solution with narration](#a-video-demonstrating-the-proposed-solution-with-narration)
* [Criteria](#criteria)
* [Appendix](#appendix)
  * [Evidence of consultation](#evidence-of-consultation)
* [Works cited](#works-cited)
<!-- TOC -->

# Criteria A: Planning
## Problem Definition
<p align="justify">As a food lover, I've identified a problem where there's no dedicated social network for food enthusiasts. We’ve limited options to connect with others online using an application, to share culinary creations and restaurant reviews. Additionally, I've had difficulties keeping notes of recipes or restaurant names on paper. Through research and consultations with others (see the <a href="https://github.com/2024sabuhiabbasov/unit4_2023-project/blob/master/README.md#evidence-of-consultation">Evidence of Consultation</a> in Appendix), I've found a need for a social network for food lovers. Existing food-related websites (Yelp: it doesn't allow sharing and discovery of recipes) and apps don't meet the needs of this community. I've tried them, but they lack specific features for food lovers (eg. following favorite users in the network, seeing only their sharings).</p>

## Proposed Solution
### Design Statement
<p align="justify">
  I'll make a website for food enthusiasts. The website's constructed using the Flask web-framework, HTML/CSS, and Python. It'll take one month to make and will be evaluated according to the criteria A.
</p>

### Rationale for Proposed Solution
<p align="justify">
  Application types include: web and mobile. Mobile applications can be accessed through only phones. This limits the number of people who can use the application. However, web-applications can be accessed through all electronic devices that have browsers. I want my application to be accessible for as many people as possible, so I decided to create a web-application.<br><br>
There're number of tools available to create a web-application: JavaScript, Python, etc. For the functionality of my web-application, I decided to use Python. One of the reasons why Python's an adequate language that has a wide range of libraries. This'll help to meet the requirements for my project as it's a large scale web-application.[2]<br><br>
SQL is designed to handle large amounts of data efficiently, making it an ideal choice for applications that need to store and manage a large amount of information. SQL databases allow for the storage of structured data, which can be easily queried. This makes SQL an adequate choice for applications that need to store critical data that must be maintained even in the event of failure.[3]<br><br>
There're several frameworks available written in the Python programming language for web-development. Well-known types of Python frameworks are Django and Flask.  
The reason behind my decision's Flask provides high level flexibility, which's crucial for web-applications that have specific requirements. Unlike other rigid frameworks (Django), Flask can work with a variety of tools, making it easy to customize to meet specific requirements, meaning users will benefit from a more personalized and customizable social network.[4]<br><br>
There're different tools for the user-interface for web-applications: React, Angular, and Vue are all popular choices. I decided to use HTML/CSS for my project.<br><br> There're several reasons behind: HTML/CSS's the foundation of the web and supported by all browsers, meaning that my project will be accessible to a wider audience, regardless of their device or platform. Secondly, HTML/CSS's highly customizable, and I can modify the design and layout of my project to fit the specific requirements of my project. This means that users will benefit from a more user-friendly and visually appealing social network.[5]</p>

<p align="right">
  <i>Word count:</i> <strong>495 words</strong>
</p>

### Success Criteria
1. *[issue tackled: “limited options to connect with others online using an application”]* The platform provides a user registration feature, allowing users to create a personal account.
2. *[issue tackled: “to share culinary creations”]* Users can CRUD operations for recipe posts with each other through the platform's sharing functionality with following values:
    - Name
    - Ingredients
    - Instructions
3. *[issue tackled: “to share culinary creations, restaurant reviews”]* The platform offers CRUD operations for restaurant reviews, allowing users to leave reviews and ratings for restaurants with following values:
    - Name
    - Location
    - Feedback
    - Rate out of 10
4. *[issue tackled: “following favorite users in the network”]* The platform provides a follow feature, enabling the network users to follow their favorite users.
5. *[issue tackled: “difficulties keeping notes of recipes or restaurant names on paper”]* The platform includes a feature that allows users to save lists of their favorite dishes.
6. _[issue tackled: “seeing only their sharings”]_ The platform allows users to see their favorite users’ posts separated from everyone’s.


# Criteria B: Design
## System Diagram
![sabubububu.png](assets%2Fsabubububu.png)
_Figure 1:_ The system diagram for the application is illustrated in Figure 1. Data is stored in social_net.db, which is facilitated by the SQLite database engine. The arrows in the diagram indicate the flow of data between the various components of the application.
## Wireframe
![Wireframe](https://user-images.githubusercontent.com/111758436/233389705-16c7192e-3e8a-49ac-851c-233865cdb49f.png)
<i>Figure 2</i> - The wireframe for the user interface is depicted in Figure 2. It shows how the website is going to look like after the development process.

## Flow Diagram
### Flow Diagram 1 - Follow Feature
![follow.jpeg](assets%2Ffollow.jpeg)
<p align="center">
  <i>Figure 3</i> - The flow diagram for the follow feature is depicted in Figure 3. It shows how the follow feature is going to work.
</p>

### Flow Diagram 2 - Login Feature
![login.jpeg](assets%2Flogin.jpeg)
<p align="center">
  <i>Figure 4</i> - The flow diagram for the login feature is depicted in Figure 4. It shows how the login feature is going to work if the fields are left blank, passwords do not match, or the user doesn't exist in the database.
</p>

### Flow Diagram 3 - New Review Feature
![new_review.jpeg](assets%2Fnew_review.jpeg)
<p align="center">
  <i>Figure 5</i> - The flow diagram for the new review feature is depicted in Figure 5. It shows how the new review feature is going to work.
</p>

## ER Diagram
![unit4ERdiagramSabu.jpg](assets%2Funit4ERdiagramSabu.jpg)
<p align="justify">
  <i>Fig. 6</i>: Entity-Relationship (ER) diagram for the Foodie network's database, illustrating the relationships between the recipes, users, reviews, and saves tables. The diagram displays one-to-many relationships using lines starting with '1' and ending with 'N', indicating the cardinality of each relationship.
</p>

<img src="https://user-images.githubusercontent.com/111758436/229475239-904e430d-e67b-4f0e-b90f-c0bf1caf982a.png" style="width:100%">
<p align="center">
  <i>Fig. 7</i>: Example Data in users Table (Note: All information is fake and does not represent real individuals or their personal information)
</p>

![img.png](assets%2Fimg_1.png)
<p align="center">
  <i>Fig. 8</i>: Example Data in recipes Table (Note: All information is fake and does not represent real posts or their authors)
</p>

![img.png](assets%2Fimg.png)
<p align="center">
  <i>Fig. 9</i>: Example Data in reviews Table (Note: All information is fake and does not represent real comments or their authors)
</p>


## UML Diagram
![unit4_UML.jpeg](assets%2Funit4_UML.jpeg)
<p align="center">
  <i>Fig. 10</i>: The UML diagram in Figure 10 illustrates the class hierarchy used in the application.
</p>

## Test plan

|	Description	|	Type	|	Input	|	Output
|	-	|	-	|	-	|	-
Test for Registration System	|	Unit Test	|	1.Open Website 2.Click on the Sign up button 3. Enter "John" for the name, "Doe" for surname. Select "Azerbaijan" for the country. Enter "johndoe123" for the username. Enter johndoe@johndoe.com for the email address. Enter "johndoelovestocook" for the password and confirm password. 4. Click the submit button on the page.	|	After clicking the submit button, it should redirect to the login page with a message on the screen saying, "Registration completed. Please log in."
Test for Error Scenario for Registration System	|	Unit Test	|	1.Open Website 2.Click on the Sign up button 3. Enter "John" for the name, "Doe" for surname. Select "Azerbaijan" for the country. Enter "johndoe123" for the username. Enter "johndoe@johndoe.com" for the email address. Enter "johndoelovestocook" for the password and confirm password with a different password. 4. Click the submit button on the page.	|	After clicking the submit button, the page should refresh, with an error message appearing at the top of the screen detailing the error saying: "Passwords do not match."
Test for Users Database	|	Integration Test	|	1.Open Website 2.Click on the Sign up button 3. Enter "John" for the name, "Doe" for surname. Select "Azerbaijan" for the country. Enter "johndoe123" for the username. Enter "johndoe@johndoe.com" for the email address. Enter "johndoelovestocook" for the password and confirm password. 4. Click the submit button on the page.	|	After successfully registering, the new user's information should be stored into the "social_net.db" database, specifically in the "users" table. Each time a user registers, their information should be added to the "users" table, ensuring the system effectively manages user data and integrates the registration process with the database operations.
Test for Login System	|	Unit Test	|	1. Open Website 2. Click on the login button 3. Enter a valid email and password for an existing user (e.g., "johndoe@johndoe.com" and "johndoelovestocook") 4. Click the login button on the page.	|	After clicking the submit button, the page should redirect to the homepage of the website
Test for error scenario for Login System	|	Unit Test	|	1. Open Website 2. Click on the login button 3. Enter an invalid email (e.g., "johndoe@gmail.com") and/or an incorrect password (e.g., "wrongpassword") 4. Click the login button on the page	|	After clicking the login button, the page should refresh, displaying an error message at the top of the screen, indicating that the login attempt has failed due to inexistent user creditentials, saying "User doesn't exist."
Test for Sharing recipe	|	Unit Test	|	1.Open Website 2.Login 3.Click New Recipe on the navigation bar 4.Enter in "Test recipe" as the recipe name,  enter "This is my first ever recipe" as the instructions, and choose "Sugar," "Flour," and "Salt" for the ingredients, 5.Click the submit button	|	After clicking the submit button, the page should redirect to the explore page of the website with "Recipe added.", displaying the new post with its Recipe Name, Instructions, Author, and Post Date.
Test for error scenario for Sharing recipe	|	Unit Test	|	1.Open Website 2.Login 3.Click New Recipe on the navigation bar 4.Leave recipe name and instructions blank and choose "Sugar," "Flour," and "Salt" for the ingredients, 5.Click the submit button	|	After clicking the submit button, the user should see a specific error message indicating that the required fields (recipe name and insturctions) are not filled in. The post should not be created or displayed on the explore page.
Test for recipes Database	|	Integration Test	|	1.Open Website 2.Login 3.Click New Recipe on the navigation bar 4.Enter in "Test recipe" as the recipe name,  enter "This is my first ever recipe" as the instructions, and choose "Sugar," "Flour," and "Salt" for the ingredients, 5.Click the submit button	|	After clicking the submit button, the new post's information should be stored into the "social_net.db" database, specifically in the "recipes" table. Each time a user creates a post, all post information should be added to the "posts" table.
Test for Editing Posts	|	Unit Test	|	1.Open Website 2.Login 3.Navigate to a post created by the logged-in user 4. Click the 'Edit' button below the post 5. Modify the recipe's name to 'My Edited Post!' and update the instructions to 'This post has been edited.' 6.Click the 'Submit' button	|	After clicking the 'Submit' button, the page should refresh and display the updated post with its new Name and Ingredients.
Test for Edited Posts Database	|	Integration Test	|	1.Open Website 2.Login 3.Navigate to a post created by the logged-in user 4. Click the 'Edit' button below the post 5. Modify the recipe's name to 'My Edited Post!' and update the instructions to 'This post has been edited.' 6.Click the 'Submit' button	|	After clicking the 'Submit' button and refreshing the page, the updated post should be reflected in the "posts" table of the "social_net.db" database.
Test for Sharing restaurant review	|	Unit Test	|	1.Open Website 2.Login 3.Click New Review on the navigation bar 4.Enter in "First restaurant review" as the name,  find "Sushiro SAKUDARIA" in the address field, write "Test feedback" for feedback and rate 8 out of 10 as rating, 5.Click the submit button	|	After clicking the submit button, the page should redirect to the explore page of the website with "Review added.", displaying the new post with its Restaurant Name, Feedback, Author, and Post Date.
Test for error scenario for Sharing restaurant review	|	Unit Test	|	1.Open Website 2.Login 3.Click New Review on the navigation bar 4.Leave the name blank,  find "Sushiro SAKUDARIA" in the address field, leave the feedback empty and rate 8 out of 10 as rating, 5.Click the submit button	|	After clicking the submit button, the user should see a specific error message indicating that the required fields (restraurant name name and feedback) are not filled in. The post should not be created or displayed on the explore page.
Test for recipes Database	|	Integration Test	|	1.Open Website 2.Login 3.Click New Review on the navigation bar 4.Enter in "First restaurant review" as the name,  find "Sushiro SAKUDARIA" in the address field, write "Test feedback" for feedback and rate 8 out of 10 as rating, 5.Click the submit button	|	After clicking the submit button, the new review's information should be stored into the "social_net.db" database, specifically in the "reviews" table. Each time a user creates a post, all post information should be added to the "reviews" table.
Test for Editing reviews	|	Unit Test	|	1.Open Website 2.Login 3.Navigate to a review created by the logged-in user 4. Click the 'Edit' button below the post 5. Modify the restaurant's name to 'My Edited review!' and update the feedback to 'This post has been edited.' 6.Click the 'Submit' button	|	After clicking the 'Submit' button, the page should refresh and display the updated post with its new Name and feedback.
Test for Edited Posts Database	|	Integration Test	|	1.Open Website 2.Login 3.Navigate to a review created by the logged-in user 4. Click the 'Edit' button below the post 5. Modify the restaurant's name to 'My Edited review!' and update the feedback to 'This post has been edited.' 6.Click the 'Submit' button	|	After clicking the 'Submit' button and refreshing the page, the updated review should be reflected in the "reviews" table of the "social_net.db" database.
Test for Saving Recipes	|	Unit Test	|	1. Open Website 2. Login 3. Navigate to a recipe post 4. Click the 'Save' button to save the post	|	After clicking the 'Save' button, the page should refresh and and return the same recipe page with "Recipe saved." message and "Unsave" button this time.
Test for Saving Recipes Database 	|	Integration Test	|	1. Open Website 2. Login 3. Navigate to a recipe post 4. Click the 'Save' button to save the post	|	After clicking the 'Like' button, a record should be stored in the "saves" table of the "social_net.db" database, reflecting the saved posts with posts' and users' ID.
Test for following user	|	Unit Test	|	1. Open Website 2. Login 3. Navigate to a post 4. Click the username 5. Press "Follow" button on the profile of the user page	|	After clicking the "Follow" button, the page should refresh and return the same page of the user with "You are now following this user." and "Unfollow" button this time.
Test for following user database	|	Integration Test	|	1. Open Website 2. Login 3. Navigate to a post 4. Click the username 5. Press "Follow" button on the profile of the user page	|	After clicking the 'Follow' button, a record should be stored in the "follow" table of the "social_net.db" database, reflecting the follows with followed and follower IDs.
Security Token Sytem	|	Functional testing	|	1. Open Website 2. Login 3. Navigate to the explore page 4. Click "Log out" button 5. Try to go back to the previous page or the homepage	|	After tryting to go back to the previous page or the homepagem, the website should redirect to the login page, and the user should be prompted to login again.
Code Review	|	Reviewing Code	|	Review the entire codebase, identifying and removing any unused code or debugging and testing artifacts, and adding comments to detail parts of code.	|	Revised version of the code that follows good coding practices, with improved readability and organization


## Record of Tasks

# Criteria C: Development
## Existing tools

| Software/Development tools | Coding Structure Tools        | Libraries       |
|----------------------------|-------------------------------|-----------------|
| PyCharm[6]                 | ORM (Object Relation Mapping) | flask[11]       |
| Python[7]                  | SQL requests                  | sqlite3[12]     |
| SQLite[8]                  | Databases                     | passlib[13]     |
| Github Copilot[9]          | Encryption                    | functools[14]   |
| CodeGPT[10]                | For loops                     |jwt[15]          |
| Jinja[27]                  | If-else statements            |dotenv[16]       |
|                            |                               |werkzeug.utils[17] |
|                            |                               |os[18]    |
|                            |                               |datetime[19]|


## List of techniques used
1. If-else statements[20]
2. Loops[21]
3. Functions[22]
4. Variables[23]
5. Lists[24]
6. Objects[25]
7. Classes[26]

## Development
### Success criteria 1: The platform provides a user registration feature, allowing users to create a personal account.
```.html
<form method="post">
    <div class="card-body">
        <h2 class="text-center">Signup form</h2>
        <div class="form-group">
            <input type="text" class="form-control" id="name" placeholder="Enter name" name="name">
        </div>
        <div class="form-group">
            <select id="country" name="country" class="form-control">
                <option value="Afghanistan">Afghanistan</option>
                <!-- The rest of the countries with alphabetical order -->
            </select>
        </div>
        <div class="form-group">
            <input type="text" class="form-control" id="username" placeholder="Enter username" name="username">
        </div>
        <button type="submit" id="button" class="btn btn-primary deep-purple btn-block ">Submit</button>
    </div>
</form>
```
This snippet of code shows the registration form. To get data from an HTML page in my Python code, I use `request` function that is a built-in function in Flask library. Forms have two methods: `methods=['GET', 'POST']`. To check if the user has tried to submit the form, I use `if request.method == 'POST'` in my Python codes. As you can see in the first line of my code above, by using `method="post"`, I specify the type of the form I want to use.

```.py
def signup():
    if request.method == "POST":
        name = request.form['name']
        country = request.form['country']
    # The rest will be shown as I explain further
```
Here you can see I try to get the values typed in the registration form. As it is written as dictionary elements (`request.form['name']`), we can see that `form` returns us a dictiniory of the typed values in the form.
```.html
<input type="text" id="name" placeholder="Enter name" name="name">
```
One interesting thing to note is the use of the `name` attribute in each input field in my HTML code. This attribute is essential for identifying the form data when it is submitted to the server as we need it to call the value from the dictionary variable.
```.py
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form['name']
        country = request.form['country']
    # The rest will be shown as I explain further
```
Using the `@app.route('/signup', methods=['GET', 'POST'])` code in my Flask application file allows me to direct all URLs to the signup page. By specifying the `/signup` URL and allowing `GET` and `POST` HTTP methods, Flask can handle requests for this URL and render the appropriate HTML template.
To render the appropriate HTML template when a user accesses the `/signup` URL, I can use the `render_template()` function provided by Flask. This function takes the name of the template file as its first argument and any additional keyword arguments representing variables to be passed to the template. Here is an example code snippet:
```.html
return render_template('signup.html', title='Sign up')
```
The title being passed in the `render_template()` function is "Sign up". The title argument is used to pass the title of the page to be displayed in the browser's title bar.
To display the value of the `title` variable in the HTML signup file, I use template tags provided by the Jinja templating engine used by Flask. The most common template tag is `{{ }}`, which allows me to output the value of a variable. Here's an example of how I use template tags in my HTML files:
```.html
{% if title %}
<title>Foodie - {{ title }}</title>
{% else %}
<title>Foodie</title>
{% endif %}
```
In this code, I use the `<title>` element for choosing a title to show in the browser's title bar. I use `{% %}`, Jinja template tag to use `if-else` statements. In the given example, `if` statement makes sure to add ' - ' after 'Foodie' if the `title` argument is given.
```.py
db = database_worker("social_net.db")
register = f"INSERT into users(name, surname, username, country, email, " \
                           f"password) values('{name}', '{surname}', '{username}', '{country}', " \
                           f"'{email}', '{encrypt_password(password)}')"
                db.run_save(query=register)
                flash('Registration completed. Please log in.', 'success')
```
So, to add user registration data to my SQLite database in Flask, I use the `database_worker` class, which returns a `Database` object that I can use to interact with the database. I create an SQL query using the user input and insert it into the `users` table using the `run_save` method of the `Database` object. This saves the data (in this situation, registration details) to the database for future use.

Additionally, I use the `flash` function to display a message to the user after successful registration. The first argument to the `flash` function is the message to be displayed, and the second argument specifies the type of the message. In this case, I use the success type to indicate that the registration was successful. This function helps me to provide feedback to the user about the outcome of their actions, which improves the user experience.

### Success criteria 2: Users can CRUD operations for recipe posts with each other through the platform's sharing functionality with following values: Name, Ingredients, Instructions
```.html
<label for="recipe-ingredients">Ingredients:</label>
<input type="text" id="ingredient-search" name="ingredient_search" onkeyup="searchIngredients()" required>
```

This code creates a label and an input field for the user to search for ingredients. The `for` attribute of the label specifies the ID of the element it labels, which in this case is the input field. This helps users with accessibility needs as they can click on the label to activate the input field.

The `type` attribute of the input field is set to  `text`, which means that the user can enter text into it. The `id` attribute specifies the unique identifier for the input field, and the `name` attribute specifies the name of the field as it will appear in the form data when the user submits the form.

I was challenged to create a text field with dynamic search. After doing some research[28] I learned how to do it. So the `onkeyup` attribute is an event handler that fires a function called `searchIngredients()` whenever the user types a key into the input field. This allows for dynamic searching as the user types, without having to submit the form each time

```.html
<script>
    function searchIngredients() {
      var searchTerm = $("#ingredient-search").val().toLowerCase();
      $(".ingredient-checkbox").each(function() {
        var ingredientName = $(this).text().toLowerCase();
        if (ingredientName.indexOf(searchTerm) >= 0) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    }
</script>
```
The function first retrieves the value of the input field, converts it to lowercase, and stores it in a variable called `searchTerm`.

The function then iterates over all HTML elements on the page with the class `ingredient-checkbox`, using the jQuery `.each()` method. For each of these elements, the function retrieves the text content of the element, converts it to lowercase, and stores it in a variable called `ingredientName`.

The function then checks whether `searchTerm` is a substring of `ingredientName`, using the `indexOf()` method. If `searchTerm` is found within `ingredientName`, the function sets the element's `display` property to `block` (i.e. the element is displayed). If `searchTerm` is not found within `ingredientName`, the function sets the element's `display` property to `none` (i.e. the element is hidden).

# Criteria D: Functionality
## A video demonstrating the proposed solution with narration

# Criteria

# Appendix
## Evidence of consultation
![Untitled design](https://user-images.githubusercontent.com/111758436/236893612-084ad4ab-47fc-476c-b162-9e15fdb2bad3.png)
<p align="justify">
  I spoke with my friend, who is also a food enthusiast, about the challenges we face in connecting with others online and sharing our culinary creations. During our chat, we discussed the need for a dedicated social network for food lovers, and I captured this screenshot to illustrate our conversation.
</p>

# Works cited
[1]: Aifnet Ltd. “Deep Dream Generator.” https://deepdreamgenerator.com/. Accessed 3 April 2023.

[2]: PODGÓRSKI, PIOTR, and MICHAŁ SŁUPSKI. “Why Use Python for Web Development? Pros, Cons, and Business Benefits.” STX Next, https://www.stxnext.com/blog/python-for-web-development/. Accessed 4 April 2023.

[3]: "SQL." W3Schools, https://www.w3schools.com/sql/. Accessed 4 April 2023.

[4]: Holovaty, Adrian, and Simon Willison. “Flask Vs Django: Which Python Framework to Choose?” InterviewBit, 29 July 2022, https://www.interviewbit.com/blog/flask-vs-django/. Accessed 4 April 2023.

[5]: CodeClan Team. “Top 5 reasons you should learn HTML & CSS.” CodeClan, 18 September 2020, https://codeclan.com/blog/top-5-reasons-you-should-learn-html-css/. Accessed 4 April 2023.

[6]: JetBrains. PyCharm Professional. Version 2023.3.2, JetBrains, 2023. Accessed Mar. 7 2023

[7]: "Python." Wikipedia, Wikimedia Foundation, https://en.wikipedia.org/wiki/Python. Accessed 7 Mar. 2023.

[8]: "SQL." W3Schools, https://www.w3schools.com/sql/. Accessed 7 Mar. 2023.

[9]: OpenAI. GitHub Copilot. Beta release, OpenAI, 2022. Accessed Mar. 7 2023

[10]: CodeGPT Documentation. Edited by OpenAI, 2021, https://code-gpt-docs.vercel.app/. Accessed Mar. 7 2023

[11]: Welcome to Flask — Flask Documentation (2.3.x). flask.palletsprojects.com/en/2.3.x. Accessed 4 April 2023.

[12]: SQLite. "SQLite Home Page." SQLite, https://www.sqlite.org/. Accessed Mar. 7 2023

[13]: Passlib. "Passlib Documentation." Read the Docs, https://passlib.readthedocs.io/en/stable/. Accessed Mar. 7 2023

[14]: “Functools — Higher-order Functions and Operations on Callable Objects.” Python Documentation, https://docs.python.org/3/library/functools.html. Accessed 4 April 2023.

[15]: “Jwt.” PyPI, 7 Oct. 2021, https://pypi.org/project/jwt. Accessed 4 April 2023.

[16]: “Python-dotenv.” PyPI, 24 Feb. 2023, https://pypi.org/project/python-dotenv. Accessed 4 April 2023.

[17]: “Werkzeug.” PyPI, 2 May 2023, https://pypi.org/project/Werkzeug. Accessed 4 April 2023.

[18]: “Os — Miscellaneous Operating System Interfaces.” Python Documentation, https://docs.python.org/3/library/os.html. Accessed 4 April 2023.

[19]: “Datetime — Basic Date and Time Types.” Python Documentation, https://docs.python.org/3/library/datetime.html. Accessed 4 April 2023.

[20]: "4.1. if Statements." Python 3.10.1 Documentation, Python Software Foundation, 2022, Accessed 7 Mar. 2023. 

[21]: Python Library. “Chapter 5: Loops.” Python 101, pythonlibrary.org, Accessed 7 Mar. 2023. 

[22]: "Functions." Easy Python Docs, Easy Python, 2023, Accessed 7 Mar. 2023. https://www.easypythondocs.com/functions.html.

[23]: "Variables." Easy Python Docs, Easy Python Docs, n.d., https://www.easypythondocs.com/variables.html. Accessed 7 Mar. 2023.

[24]: Code Fellows. “Python Data Structures: Arrays and Lists.” Code Fellows, n.d., https://codefellows.github.io/sea-python-401d4/lectures/array.html. Accessed 7 Mar. 2023.

[25]: Python Software Foundation. "Objects, Values, and Types." Python 3.9.7 documentation, 2021, https://docs.python.org/3/reference/datamodel.html#objects-values-and-types. Accessed 7 Mar. 2023.

[26]: Python Software Foundation. “9. Classes.” Python 3.10.0 documentation, Python Software Foundation, 2021, https://docs.python.org/3/tutorial/classes.html. Accessed 7 Mar. 2023.

[27]: Jinja — Jinja Documentation (3.1.x). jinja.palletsprojects.com/en/3.1.x. Accesssed 4 April 2023.

[28]: “Dynamic Search.” CodePen, codepen.io/coltonf93/pen/DbagWg. Accessed 18 April 2023.
