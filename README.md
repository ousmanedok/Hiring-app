# Hiring-app

## How to Install

 1. Clone the repository: `git@github.com:ousmanedok/hiring-app.git`
 2. Make a copy of the `env` file and rename it `.env`
 3. Add your database credentials and other env variable to this file
 4. Set up and activate a virtual environment
 5. Install the required python packages: `pip install -r requirements.txt`

## Start the Project

1. Start the dev server: `./manage.py runserver`
2. In your browser go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Coding Standard

Before committing your changes run the following commands:

    flake8 .
    black .
    isort .
Note: Fix the issues highlighted by flake8 before moving to the next command. 
