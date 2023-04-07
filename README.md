# Foodie: A Social Network for Food Lovers
<img src="https://user-images.githubusercontent.com/111758436/229414078-7b5067ff-7633-4fb9-9ec2-4d1091d0e5e3.png" style="width:100%">
<p align="center">
  <i>Fig. 1</i>: Using the prompt 'Generate a picture of a cozy kitchen with ingredients and utensils for cooking a delicious meal in a rustic and warm colors,' this image was generated using AI on Deep Dream Generator.
</p>

# Criteria A: Planning
## Problem Definition
<p align="justify">As a food lover, I have identified a problem where there is no dedicated social network for food enthusiasts. We have limited options for food enthusiasts to connect with others online, limited options to share culinary creations, and difficulty finding specific recipes or restaurant recommendations online. Through research and consultations with other food enthusiasts (see the <a href="https://github.com/2024sabuhiabbasov/unit4_2023-project/blob/master/README.md#evidence-of-consultation">Evidence of Consultation</a>), I have found a need for a dedicated social network for food lovers. Existing food-related websites (eg. Yelp: it doesn't allow for easy sharing and discovery of recipes) and apps don't meet specifically to the needs of this community. I have tried them, but they lack specific features for food lovers.</p>

## Proposed Solution
### Design Statement
I will design and make a website for food enthusiastics. The website is constructed using the Flask web framework, HTML/CSS, and Python. It will take one month to make and will be evaluated according to the criteria A.
### Rationale for Proposed Solution
The chosen technology tools for the food enthusiast social network project include Flask, Python, HTML/CSS, and SQLite. Flask was chosen as the web framework due to its simplicity, flexibility, and extensibility, making it well-suited for building scalable and efficient web applications.[^1] Python was selected for its ease of use, readability, and extensive library support, making it a popular choice for web development.[^2] HTML/CSS was chosen for its ability to create user-friendly and visually appealing interfaces, which is particularly important for a social network platform.[^3] Finally, SQLite was selected for its simplicity and ease of use for small-scale database management.[^4]

These technology tools were carefully evaluated and selected based on their suitability for the project's specific needs, rather than personal experience or familiarity. Extensive research was conducted to identify the most appropriate tools for building a dedicated social network for food enthusiasts. The use of SQLite highlights that data management has been carefully considered in the proposed solution, ensuring that the website can handle large amounts of data efficiently.

Therefore, the selection of technology tools for the food enthusiast social network project is justified in the context of the project's specific requirements and has been chosen based on extensive research and evaluation.
### Success Criteria
1. The platform provides a user registration feature, allowing users to create a personal account.
2. Users can easily share recipes with each other through the platform's sharing functionality.
3. The platform offers a restaurant review feature, allowing users to leave reviews and ratings for restaurants.
4. Users are able to make edits to their own posts on the platform.
5. The platform provides a search functionality that allows users to easily find and filter through recipes and restaurant reviews.
6. The platform includes a feature that allows users to create and save lists of their favorite restaurants and dishes.

# Criteria B: Design
## System Diagram
## Wireframe
## Flow Diagram
## ER Diagram
<img src="https://user-images.githubusercontent.com/111758436/230533070-1de92db9-e160-4a9b-8f98-ee646fd35cb9.jpg" style="width:100%">
<p align="justify">
  <i>Fig. 6</i>: Entity-Relationship (ER) diagram for the Foodie network's database, illustrating the relationships between the Users, Posts, and Comments tables. The diagram displays one-to-many relationships using lines starting with '1' and ending with 'N', indicating the cardinality of each relationship.
</p>
<img src="https://user-images.githubusercontent.com/111758436/229475239-904e430d-e67b-4f0e-b90f-c0bf1caf982a.png" style="width:100%">
<p align="center">
  <i>Fig. 7</i>: Example Data in Users Table (Note: All information is fake and does not represent real individuals or their personal information)
</p>
<img src="https://user-images.githubusercontent.com/111758436/229518547-acdfb0b0-8905-442c-951a-038e89c16932.png" style="width:100%">
<p align="center">
  <i>Fig. 8</i>: Example Data in Posts Table (Note: All information is fake and does not represent real posts or their authors)
</p>
<img src="https://user-images.githubusercontent.com/111758436/229649561-11764057-4ff2-430c-ba24-d151bcecba67.png" style="width:100%">
<p align="center">
  <i>Fig. 9</i>: Example Data in Comments Table (Note: All information is fake and does not represent real comments or their authors)
</p>


## UML Diagram
## Test plan
## Record of Tasks

# Criteria C: Development
## Existing tools
## List of techniques used
No definition!  
## Development
Explain how I was challenged and how I solved with explaining the lines of codes.

# Criteria D: Functionality
## A video demonstrating the proposed solution with narration

# Appendix
## Evidence of consultation
![unit-4-problem-consultation](https://user-images.githubusercontent.com/111758436/230363742-b80cf48b-731d-4559-b3d3-5e9a917fade9.png)
<p align="justify">
  I spoke with my friend, who is also a food enthusiast, about the challenges we face in connecting with others online and sharing our culinary creations. During our chat, we discussed the need for a dedicated social network for food lovers, and I captured this screenshot to illustrate our conversation.
</p>

# Works cited
[^1]: Grinberg, Miguel. "The Flask Mega-Tutorial Part I: Hello, World!" Miguel Grinberg's Blog, 3 Apr. 2021, https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world. Accessed 2 Apr. 2023.
[^2]: Python Software Foundation. Python, Python Software Foundation, https://www.python.org/. Accessed 2 Apr. 2023.
[^3]: "W3Schools Online Web Tutorials. HTML/CSS Tutorial." W3Schools, 2023, https://www.w3schools.com/html/html_css.asp. Accessed 2 Apr. 2023.
[^4]: sqlite tutorial. (n.d.). SQLite Tutorial - An Easy Way to Master SQLite Fast. Retrieved October 10, 2021, from https://www.sqlitetutorial.net/ Accessed 2 Apr. 2023.
