## BREW_NEIGHBOURHOOD
## Description
A django web application that allows users be in the loop about everything happening in their neighbourhood.From contact information of handy man to meeting announcements or even alerts
## User Story
As a user I would like to:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
Only view details of a single neighborhood.
## Setup and Installations
* git clone https://github.com/Lomemoraine/BREW_NEIGHBOURHOOD.git
* Initialize git and add the remote repository
* git init
* git remote add origin <your-repository-url>
* Create virtual environment

  $ python3.9 -m virtualenv virtual
* Activate the virtual environment

  $ source virtual/bin/activate
* Setting up environment variables

Create a .env file and paste paste the following filling where appropriate:

* SECRET_KEY = 'SECRET_KEY'
* DEBUG=True
* DB_NAME='<your database name>'
* DB_USER='<your database name>'
* DB_PASSWORD='<password to your database>'
* DB_HOST='127.0.0.1'
* MODE='dev'
* ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
* DISABLE_COLLECTSTATIC=1
Install dependancies

Install dependancies that will create an environment for the app to run pip 

* install -r requirements.txt

Make and run migrations

* python3.9 manage.py check
* python manage.py makemigrations posts
* python3.9 manage.py sqlmigrate posts 0001
* python3.9 manage.py migrate

Run the app

* python3.9 manage.py runserver
* Open localhost:8000

Testing the Application

* python manage.py test posts
## Technology used
* Python3.9
* Django 4.0.5
* Postgresql
* Boostrap
* HTML
* CSS
## Support and Contact details
Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :@memo_lorraine

