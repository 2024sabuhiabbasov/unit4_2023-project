# Foodie: A Social Network for Food Lovers
<img src="https://user-images.githubusercontent.com/111758436/229414078-7b5067ff-7633-4fb9-9ec2-4d1091d0e5e3.png" style="width:100%">
<p align="center">
  <i>Fig. 1</i>: Using the prompt 'Generate a picture of a cozy kitchen with ingredients and utensils for cooking a delicious meal in a rustic and warm colors,' this image was generated using AI on Deep Dream Generator.[1]
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
    - Preparation
3. *[issue tackled: “to share culinary creations, restaurant reviews”]* The platform offers CRUD operations for restaurant reviews, allowing users to leave reviews and ratings for restaurants with following values:
    - Name
    - Location
    - Feedback
    - Rate out of 10
4. *[issue tackled: “following favorite users in the network”]* The platform provides a follow feature, enabling the network users to follow their favorite users.
5. *[issue tackled: “difficulties keeping notes of recipes or restaurant names on paper”]* The platform includes a feature that allows users to create and save lists of their favorite restaurants and dishes.
6. _[issue tackled: “seeing only their sharings”]_ The platform allows users to see their favorite users’ posts separated from everyone’s.


# Criteria B: Design
## System Diagram
## Wireframe
![Wireframe](https://user-images.githubusercontent.com/111758436/233389705-16c7192e-3e8a-49ac-851c-233865cdb49f.png)
<i>Figure 2</i> - The wireframe for the user interface is depicted in Figure 2. It shows how the website is going to look like after the development process.

## Flow Diagram
## ER Diagram
![unit4ERdiagramSabu.jpg](assets%2Funit4ERdiagramSabu.jpg)
<p align="justify">
  <i>Fig. 6</i>: Entity-Relationship (ER) diagram for the Foodie network's database, illustrating the relationships between the recipes, users, reviews, and saves tables. The diagram displays one-to-many relationships using lines starting with '1' and ending with 'N', indicating the cardinality of each relationship.
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

# Criteria

# Appendix
## Evidence of consultation
![unit-4-problem-consultation](https://user-images.githubusercontent.com/111758436/230363742-b80cf48b-731d-4559-b3d3-5e9a917fade9.png)
<p align="justify">
  I spoke with my friend, who is also a food enthusiast, about the challenges we face in connecting with others online and sharing our culinary creations. During our chat, we discussed the need for a dedicated social network for food lovers, and I captured this screenshot to illustrate our conversation.
</p>

# Works cited
[1]: Aifnet Ltd. “Deep Dream Generator.” https://deepdreamgenerator.com/. Accessed 3 April 2023.

[2]: PODGÓRSKI, PIOTR, and MICHAŁ SŁUPSKI. “Why Use Python for Web Development? Pros, Cons, and Business Benefits.” STX Next, https://www.stxnext.com/blog/python-for-web-development/. Accessed 4 April 2023.

[3]: "SQL." W3Schools, https://www.w3schools.com/sql/. Accessed 4 April 2023.

[4]: Holovaty, Adrian, and Simon Willison. “Flask Vs Django: Which Python Framework to Choose?” InterviewBit, 29 July 2022, https://www.interviewbit.com/blog/flask-vs-django/. Accessed 4 April 2023.

[5]: CodeClan Team. “Top 5 reasons you should learn HTML & CSS.” CodeClan, 18 September 2020, https://codeclan.com/blog/top-5-reasons-you-should-learn-html-css/. Accessed 4 April 2023.
