# Django Starter Temmplate


This is a skeleton and a guide to add the most common packages to a
Django project. This is inspired by django-party-pack and I'm tired of
doing the same things each time I start a Django project and having to
look up the documentation because I don't remember how to do it.

## Virtualenv

Activate the environment::

    $ workon myenv

Install requirements::

    $ pip install -r requirements.txt


### Gitignore

(Because you are obviously using git)

Create a `.gitignore` file in the project's root and add the patterns
you don't want to have under version control.

Here are some useful patterns to ignore::

    *.pyc
    env/
    *~
    *.log
    .coverage
    _build
    db.sqlite3

Here is a very usefull list of .gitignore patterns for different
projects https://github.com/github/gitignore

Documentation
=============

## Getting Started

1.  Clone the repository

         git clone https://github.com/AAshutoshShrestha/Django_Template_with_Bootstrap.git {{ your project name }}

    Alternately you can download the zip file and unzip it.

2.  You will now have the cloned project folder. Open the project in
    Visual Studio Code editor

3.  Project structure is like:::

          project_name
          │   ├───app_name
          │   │   ├───migrations
          │   │   │   └───__pycache__
          │   │   └───__pycache__
          │   ├───media
          │   ├───project_name
          │   │   └───__pycache__
          │   ├───static
          │   │   ├───css
          │   │   ├───img
          │   │   └───js
          │   └───template
          │   │   ├───admin
          │   │   └───view
          │   ├───db.sqlite3
          │   ├───manage.py

4.  Run server

        python manage.py runserver


## How to use

-   Rename the Project_name and app_name as your project requirements.
-   Change the appname on project_name>setttings.py
-   On appname>apps.py update name field as your app name
-   on app_name>>admin.py update navbar links as required 
-   update Models.py and enter::
        python manage.py makemigrations
        python manage.py migrate
-   Running project on localhost. Initial URL is  localhost:5000/home
-   Change the template files base.html, home.html
-   Admin access
         username : admin
         Password : admin@123
