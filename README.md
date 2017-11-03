## Django News Articles
DISCLAIMER: This is only for use in Development environments right now.

Todo: Unit tests

### Overview
Django Application that collects news source & articles using Celery Beat scheduled tasks. Uses the django rest framework for fetching API data.

Once collected, articles and relevant links are kept in the database and loaded from:

 - /articles/articles (Last 100 entires HTML View)
 - /articles/json	(Last 100 entires JSON View)

### Installation

#### Linux pre-requisite packages (Tested with 16.04 Ubuntu)

sqlite3
python2.7
pip
virtualenv
rabbitmq-server

To install these requirements:

`sudo apt-get update`

`sudo apt-get install -y python2.7 python-pip sqlite3 virtualenv rabbitmq-server`

#### Development Deployment

To deploy in development, clone this repo and create a virtualenv inside the repo: `virtualenv env`

Start the virtualenv: `source env/bin/activate`

Install the requirements `pip install -r requirements.txt`

Update API_KEY with your newsapi.org API KEY and SECRET_KEY with a random string in the `settings.py` file.

Create the Django DB (Sqlite3 by default): `python manage.py migrate`

Run the Django application: `python manage.py runserver localhost:8080`

Run the Celery worker (From a new terminal with the virtualenv enabled): `celery -A  reachlocalnews worker -l info -B`

From your browser, navigate to:

http://localhost:8080/articles/articles - HTML

http://localhost:8080/articles/JSON 	- JSON

(Note this will take up to 120 seconds to populate the DB)

#### Admin Access
Models are registered to the admin panel. If interested in seeing the models, remember to create a superuser: `python manage.py createsuperuser`

You can access the admin panel from: http://localhost:8080/admin
