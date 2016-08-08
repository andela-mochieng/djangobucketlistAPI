[![Coverage Status](https://coveralls.io/repos/github/andela-mochieng/djangobucketlistAPI/badge.svg?branch=develop)](https://coveralls.io/github/andela-mochieng/djangobucketlistAPI?branch=develop)
![alt text](https://img.shields.io/badge/python-2.7-blue.svg)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]()

# djangobucketlistAPI
BucketlistAPI built with django/-restframework and Angular2

### Bucketlist's resources
The API resources are accessible at [localhost:8000/api/v1.0/](http://127.0.0.1:8000/api/v1.0/). They include:

| Resource URL | Methods | Description |
| -------- | ------------- | --------- |
| `/api/v.1/` | GET  | The index |
| `/api/v.1/register/` | POST  | User registration |
|  `/api/v.1/api-token-auth/` | POST | Obtain login token |
| `/api/v.1/bucketlists/` | POST | Create a bucket list |
| `/api/v.1/bucketlists/` | GET | Retrieve all bucketlists |
| `/api/v.1/bucketlists/?limit=1&page=1` | GET | Retrieve one bucketlist per page|
| `/api/v.1/bucketlists/<id>/` | GET |  A single bucket list |
| `/api/v.1/bucketlists/<id>/` | PUT | Update a single bucket list |
| `/api/v.1/bucketlists/<id>/` | DELETE | Delete a single bucket list |
| `/api/v.1/bucketlists/<id>/items/` | POST |  Create items in a bucket list |
| GET `/api/v.1/bucketlists/<id>/items/<item_id>/` | PUT, DELETE| A single bucket list item|


| Method | Description |
|------- | ----------- |
| GET | Retrieves a resource(s) |
| POST | Creates a new resource |
| PUT | Updates an existing resource |
| DELETE | Deletes an existing resource |


###### The key **libraries** used include;
1. **Django** - A high level python framework that enables rapid web app development.
2. **django-rest-swagger** - An API documentation generator
3. **djangorestframework** - A toolkit for building web Api's.
4. **djangorestframework-jwt** - Is a token-based authentication mechanism for clients to obtain a JWT given the username and password.
5. **coverage, coveralls, nose** - Modules used for testing and viewing test coverage.
6. **django-cors-headers** -  CORS builds on top of XmlHttpRequest to allow my  Angular built front-end to make cross-domain requests, similar to same-domain requests.
7. **gunicorn** - Is a server that is called with the location of a module containing a WSGI application. E.g `gunicorn bucketlist.wsgi`


## Installation
1. **__Clone this repo__**
```shell
$ git clone https://github.com/andela-mochieng/djangobucketlistAPI.git
```

2. **__Set up a virtualenv then:__**
```shell
$ pip install -r requirements.txt
```

3. **__Nagivate to the root folder__**
```shell
$ cd djangobucketlistAPI
```

4. __Navigate to bucketlist/settings/dev.py and config your database settings__
###Set up a local database configurations

```shell
"""
Development specific settings.
"""
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bucketlist', # Enter your database's name
        'USER': 'postgres', # Enter your DB user
        'PASSWORD': 'codango', # Enter your DB password
        'HOST': '0.0.0.0',
        'PORT': '5432',
    }
}
```


```shell
5. Run `$ python manage.py makemigrations` and `$ python manage.py migrate` to create the necessary tables  required to run the application.
6. Run `$ python manage.py runserver` to run the app.
7. Run `$ coverage run manage.py test` to know  theautomated test coverage.
8. Run `$ coverage report` to view the report of the coverage on your terminal.
9. Run `$ coverage html` to produce the html of coverage result.
```






