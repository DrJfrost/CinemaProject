# CinemaProject
A project for Software Engineering program, Manager of cinema tickets

## Installation

1. clone the repository
2. activate virtual environment of python if you have any
`source venv/bin/activate`
3. go in the terminal to the repository folder and install dependencies
`pip install -r requirements.txt`
4. configure the Database on the `settings.py` file according to your systems DB config

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #insert postgresql Engine for Postgres
        'NAME': 'cinedistrito_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306', #port of the db
    }
}
```
5. make migrations on terminal
`python manage.py makemigrations`
6. Run migrations on terminal
`python manage.py migrate`
7. load all initial data (fixtures) on terminal
`python manage.py loaddata */fixtures/*.json`
8. finally run the server on terminal :)
`python manage.py runserver`

---
**Note:** All of the endpoint usage documentation is on the postman file `cinedistritoAPI.postman_collection.json` make sure to import it as a collection on postman


