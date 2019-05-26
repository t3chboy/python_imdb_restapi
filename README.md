## RESTFul APIs for imdb movie module.
![PYTHON](https://img.shields.io/badge/Python-Powered%20by%20Flask-brightgreen.svg?longCache=true&style=for-the-badge)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)]()

Problem 1: Movie Data Collection (RESTful apis, only backend)

Write API:
- create/delete/view Movie Data Collection.
  - [x] POST to create movie and genre record
  - [x] DELETE to delete movie record.
  - [x] View all movie records.
  
 
 ## Technical Details : 

#### Tech Stack
    Python
    Mysql
    
#### Packages Used
    "Flask": "1.0.3",
    "flask_marshmallow": "0.10.1",
    "Flask_RESTful": "0.3.7",
    "SQLAlchemy": "1.3.3",
    "marshmallow": "2.19.2",
    "pip": "19.1.1"
 
#### Setup
    - Get all the dependencies installed.
#### Database setup
    - Get Mysql installed.
    - Create database - imdb
    - Change mysql credentials in __init__.py
    - Import imdbapis.sql to database. 
#### APIs Documentation and Usage
- [API DOCUMENTATION](https://documenter.getpostman.com/view/3407371/S1TR6LaB)
- Import `imdb_python_restapi.postman_collection.json` collection in postman to run the APIs. 

#### Use Application
- [x] Browse to root folder of app via terminal.
- [x] Type `env/bin/python run.py` to start the application.
- [x] Hit the APIs from postman collection imported ealier.

#### Check ERROR logs
  - All application and mysql logs are printed on the terminal itself since its inbuilt funtionality itself.
  
  #### Developer Notes
- For scalability and to handle huge traffic we can use In Memory database like Redis.
- Here we are using Mysql RDBMS, for which we are using connection pooling technic, so that we can cache and resuse connections.  Current pool size = 100.
- Folder Structure
  1. Controller - All Rest based controllers which get the request from routes and pass it to models.
  2. Models - All Models are related to each controller and they perfome database realted operations.
  3. Routes - To handle all http request based on http methods we have defined them in run.py
  4. Python Packages : Conatins 3rd party packages.
  5. Flask : Python based framework.
  6. Flask-RESTful : Python based Restful Api framework.
  7. Flask-SQLAlchemy : Flask based support for Sqlalchemy
  10. Sqlalchemy : The Python SQL Toolkit and Object Relational Mapper.

## More Problem Statements :
Since We had requirment to handle traffic approx ~15M Apis
  So we used minimalistic flask, as its fast low overhead api framework, for Python.
  
##For Scaling this monolithic app we can consider below implmentation :

  - We can also use `Redis` for data storage since movie data doesnt change once created frequently and this help reduce DB calls.
  
  - We can also store data using `ElasticSearch` based on `genres`, since its inverted index helps to fetch data more faster than using Mysql Joins.
  
  - We can also add a initial API Gateway layer like `Netflix ZUUL` or `Nginx Kong` to reduce overhead on app, as many static request and bad request can be responded from here and also we can perform Authentication, request throttling, request metrics and security validations with this. 
  
  - We can use `microservice` based architecture to scale our application X times.
    1. While runnning marketting campaign for a particular movie or genre.
    2. Release of a particular movie. 
  
  - Major bottle neck would be Mysql joins, so for this based on time period we can store early data in elasticseacrh or Redis depending on product requirment, 
  eg: 
  - Collecting all Freedom fighting movies in single document during Independenace Day.
  - Collecting all Animation and children movies in single document during vaccations.
  
  - We can also have front end `cache controls` using response headers for GET request with cache timeouts.
  
  - We should also store and study users made `GET search` request, so we can apply ML/AI on this activities and provide more user preferred and personalize recommendation.

  
    
