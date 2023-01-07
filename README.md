# Search Backend API
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

## How to setup Search Backend API
1. Clone this repo.
2. Create virtual environment with name **venv**.
3. Activate the virtual environment.
4. Install dependences from requirements.txt file
5. Install MongoDB 
6. Create Database search_app_db
7. Import data from users, tickets and organizations into MongoDB Collections

## Clone and install dependencies
##### clone repo

```shell
git clone https://github.com/tabraizyaseen/search_backend.git
git checkout main
```
##### create and activate virtal envoirnment
```shell
python3 -m venv venv

# activate virtual envoirnment
source venv/bin/activate
```

##### Install Dependencies
```shell
pip install -r  requirements.txt
```

##### Create search_backend/secrets.py file
```shell
SECRET_KEY = 'django-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# mongo creds
MONGO_USER = "mongo_user"
MONGO_PASS = "mongo_pass"
MONGO_PDA_HOST = "127.0.0.1:27017"
search_database = 'search_app_db'
users_search_col = 'users'
organizations_search_col = 'organizations'
tickets_search_col = 'tickets'

MONGO_DATABASE_HOST = "mongodb://" + MONGO_USER + ":" + MONGO_PASS + "@"+MONGO_PDA_HOST+"/?authSource=admin" 
```

##### Run django server
```shell
python manage.py runserver 8000
```

##### Import postman collection from 'Search Backend.postman_collection.json' file

## Road Map/Future Plan
- Writing Django unit tests
