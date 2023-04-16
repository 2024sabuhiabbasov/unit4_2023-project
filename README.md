# Foodie: A Social Network for Food Lovers
<img src="https://user-images.githubusercontent.com/111758436/229414078-7b5067ff-7633-4fb9-9ec2-4d1091d0e5e3.png" style="width:100%">
<p align="center">
  <i>Fig. 1</i>: Using the prompt 'Generate a picture of a cozy kitchen with ingredients and utensils for cooking a delicious meal in a rustic and warm colors,' this image was generated using AI on Deep Dream Generator.
</p>

# Criteria A: Planning
## Problem Definition
<p align="justify">As a food lover, I have identified a problem where there is no dedicated social network for food enthusiasts. We have limited options for food enthusiasts to connect securely with others online using a web-application, limited options to share culinary creations, and difficulty finding specific recipes or restaurant recommendations online. Additionally, I have had difficulties to keep notes of recipes or restaurant names on paper. Through research and consultations with other food enthusiasts (see the <a href="https://github.com/2024sabuhiabbasov/unit4_2023-project/blob/master/README.md#evidence-of-consultation">Evidence of Consultation</a> in Appendix), I have found a need for a dedicated social network for food lovers. Existing food-related websites (eg. Yelp: it doesn't allow for easy sharing and discovery of recipes) and apps don't meet specifically to the needs of this community. I have tried them, but they lack specific features for food lovers.</p>

## Proposed Solution
### Design Statement
I will design and make a website for food enthusiastics. The website is constructed using the Flask web framework, HTML/CSS, and Python. It will take one month to make and will be evaluated according to the criteria A.
### Rationale for Proposed Solution
Application types include web and mobile application. Mobile applications can be accessed through only mobile devices. This puts a limit in the number of people who can use the application. However, web applications can be accessed through all electronic devices that have browser. As I want my application to be accessible for as much people as possible, I decided to create a web-application.

There are number of tools available to create a web application: JavaScript, Python, etc. For the functionality of my web-application, I decided to use Python language. One of the reasons why Python is an adequate language to use for web applications is that it has a wide range of libraries. This will help me to meet the requirements for the social network as it is a large scale web application. Secondly, Python has a built-in database management system, allowing us to handle large amount of data without any concerns. This is essential for a social network to manage data of hundreds of users using the social network efficiently. (PODGÓRSKI and SŁUPSKI)

To create a website using Python, there are several frameworks available. The most famous Python frameworks are Django and Flask.


### Success Criteria
1. The platform provides a user registration feature, allowing users to create a personal account.
2. Users can share recipes with each other through the platform's sharing functionality.
3. The platform offers a restaurant review feature, allowing users to leave reviews and ratings for restaurants.
4. Users are able to make edits to their own posts on the platform: modify and remove.
5. The platform provides a search functionality that allows users to find and filter through recipes and restaurant reviews:

    a) By A-Z

    b) By date

    c) By category

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
[^1]: PODGÓRSKI, PIOTR, and MICHAŁ SŁUPSKI. “Why Use Python for Web Development? Pros, Cons, and Business Benefits.” STX Next, https://www.stxnext.com/blog/python-for-web-development/. Accessed 4 April 2023.
