# flask_base

A basic template for flask app development.

## Dependency 

Dependencies listed below should be installed in your environment.

*virtualenv is recommended*

* flask
* sqlalchemy
* flask-sqlalchemy
* sqlalchemy-migrate

##Usage

For the first time, empty sqlite database should be generated: 

'''
$ python db_create.py
'''

Start development server for debugging: 

'''
$ python run.py
'''

The template app will be running on
'''
http://localhost:5000
'''

##License

MIT
