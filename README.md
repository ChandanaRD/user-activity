# User-Activity
A Django application for user and activity model 

Application is hosted on heroku: https://user-activity-2020.herokuapp.com/

## About Project
This project uses sqlLite3 DB. 
models -> User, ActivityPeriod
template -> One view to display all users and activities in a json

## Run the application

#### Migrate DB data
python manage.py migrate
#### Start Server
python manage.py runserver

## Create data using shell
python manage.py shell

## Generate data using Custom Management Command

#### Open heroku bash
heroku run bash -a user-activity-2020

#### Run custom management command
python manage.py load_dummy_user_data

* arguments: --users 1
    * generates 1 user entry by default, this number can be modified.