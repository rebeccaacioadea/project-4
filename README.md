

![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)
General Assembly, Software Engineering Immersive

# Poppins
 [](http://poppins-books.herokuapp.com/)
 
###A Flask & React Application
A Plant Baby Sitting App

## Overview 
This is my final project at General Assembly as a Software Engineer Immersive course's student. We were placed in a group of 3 to worked together to design and develop a full stack application within 6 days. This project required us as a team to build both backend and front-end using technologies such as PostgreSQL, Python, Flask and React.

Poppins is an app where young readers and their parents can share the views  about a book and can also make recommendation to their fellow readers. 


### Brief:

* Collaborative development using Git and GitHub.
* Build a full-stack application by making your own backend and front-end.
* Use a Python Flask API by using a Flask REST framework to serve the data from a Postgres database.
* Consume your API with a separate front-end built with React.
* Be a complete project with multiple relationships and CRUD functionality for at least a couple of models.
* Implement thoughtful user stories/wireframes and identifying the features that were core to MVP.
* Design a visually impressive Front End, with mobile responsiveness as a key element.
* Be deploy online and accessible to the public.

### Technologies:

* HTML
* SCSS
* JavaScript
* React.js and JSX 
* Node Package Manager (npm)
* Babel Transpiler
* Webpack
* Python
* Flask
* PostgreSQL
* Marshmallow and SQLAlchemy
* Insomnia
* VSCode
* Git 
* GitHub 
* Herokun(Deployment)


## Functionality: 

User should be able to:
* Register and
login into our app.

* Update and delete their account.
* Add, update or delete books in their profile.
* Make comments and recommendation on books.

## Approach taken:



### Planning 
On the first we discussed the full-stack app we wanted to design and build as a team and then we work through the backend framework together.
We look at different features we wanted the app to have. We had to look into what our models and their relationship with each other might look like for our data.
We also identify on day 1 that we will need an external API for this project, therefore we had to find the API that was able to give us the information required.
Additionally, we looked at what CRUD we would like our API to use

Below is a copy of the planning for our backend development we came out with this project.
 
![](https://i.imgur.com/80jouat.png)

## Endpoints
Although we had created, we wanted to use an external API along with our own API we had created. We had some issues with obtaining the 'API_Key', therefore, we ended up manually seeding the data.


### The Backend 

We started developing the backend together through *'Zoom Screenshare'*. Starting with server.js, models (for our data, message and user), router.js and controllers.
For each stage we tested on the ***'terminal'*** and ***'Insomnia'*** to see our codes were written correcting without a bug before moving onto the next task.

Examples of our backend structures: models, serializers, controllers etc

![](https://i.imgur.com/HI1B0VKm.png)


Example of the structure of Basemodel for the database 
![](https://i.imgur.com/I9GznZO.png)

Example of the structure of 'book' model
![](https://i.imgur.com/KVH8BtHl.png)

Example of the structure of the many-to- many (M-M) relationship between the models for our data.
![](https://i.imgur.com/xsNP6vg.png)

Example of the serializer for our 'Books' data
![](https://i.imgur.com/FciMJ4z.png) 


When the user needs to add, update or delete a plant, message or a comment, we created authentication process through ***secure route***. Therefore, a user can only post on the app if they are registered and have logged in on the app and they can only update or delete what they have posted.
Below is the authentication for a user that is logged in.
![](https://i.imgur.com/PyeHLtq.png)
We used the JSON Web Token (jwt) method to generate authentication.


### The Frontend with React
After creating the fundamental of the Backend, we started working on the Front-end. 
When we were working on the front-end, we realised that the 'relationship' between some of the models were incorrect, so I had to go back to the backend and make the correction before joining the rest of the team on the fort-end. 

We briefly went through the components for the frontend and setted it up together through *'Zoom Screenshare'*. 

We used React hooks, useState and useEffect along with axios to fetch data from our internal API. 


## Summary


In our group we had to communicate effectively and respect each other's opinions and be supportive as we are all still learning. 
From the beginning we recognised and acknowledged each other strength, and we worked together effectively, ensuring we communicated regularly about our progress on the project.

This is my most proud project because I learnt so much while developing this application and I had to assist my team members in debugging any problem that may arise due to conflicts after merging or syntax error or anything else that needed attention.  

In the end, my team and I had put together and deployed an app that I am very happy with. It looks amazing and it is easy to use.
It had been an amazing experience to build a full-stack application using two different programming languages (Python Flask for the backend and JavaScript, React.js for the front-end).


## Contributors


[Rebecca](https://github.com/rebeccaacioadea)

[Sagal](https://github.com/sagalosman)

[James](https://github.com/JamesPBolton)




