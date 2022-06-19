### Brew Neighborhood

> A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

> Live demo [ ]

### Project Contributors

> Lorraine Chepkemoi
> Danis Muga
> Maureen Muriithi
> Bianca Nyambura
> Fridah Kitunguu
> Joylene Kirui

### Table of Contents

- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [User Story](#user-story)
- [Setup/Requirements](#setup/requirements)
- [Behavior Driven Development](#test-driven-development)
- [Test Driven Development](#test-driven-development)
- [Known Bugs](#known-bugs)
- [License](#license)


#### Screenshots
Home
[![homepagehood.jpg](https://i.postimg.cc/C1JHH1by/homepagehood.jpg)](https://postimg.cc/mzzHTTdV)

#### Technologies Used

- HTML
- CSS (Bootstrap)
- Python
- Django
- JavaScript
- Postgres
- Google fonts
- Browsers

#### User Story
The user is able to:
1. Sign in to the application to start using it.
2. Set up a profile which contains:
    - My name
    - My location
    - My neighborhood name
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the emergency services
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.

#### Setup Requirements 
- Ensure you have the following installed on your machine
    - python3.7 or later
    - django
    - pip
    - virtual enviroment
    - Postgress database

    ## Dependencies
    All dependencies are listed in the requirements.txt file

    ## Clone
    git clone https://github.com/Lomemoraine/Awwwards_Clone.git
    cd BREW_NEIGHBORHOOD_Clone
    Open in your preferred IDE(Vs Code ,Pycharm,atom)

    ## Running the application
    - To run the application, open the cloned file in terminal and run the following commands: * python3 manage.py runserver

    ## Make and Run Migrations

    * python3.8 manage.py check
    * python manage.py makemigrations 
    * python3.8 manage.py sqlmigrate 
    * python3.8 manage.py migrate

#### Behavior Driven Developmant
- The user lands on landing page where they can join a hood.
- A user can register and login into the apllication.
- A user can update their profile using the admin dashboard.
- An authenticated user can post their posts/business for others to view in their neighborhood.
- An authenticated user can join, exit or change neighorhoods.


#### Test Driven Development
- All the tests can be runned by typing the following command on the terminal $Python3 manage.py test

#### Known Bugs

I have no any known bugs.
However, we are yet to redirect the businesses and posts to the single hood page.

#### License

This project is open source and available under the [MIT License]




