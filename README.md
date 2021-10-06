# Offers

# How to use
- Download the repository
```
git clone https://github.com/rehan-mateusz/Offers/
```

- Create .env file in Offers/offersproject/offersproject/ it should contain:
```
SECRET_KEY=your_SECRET_KEY
DEBUG=on
```

- Start with docker:

cd to /Offers and use docker-compose by typing in console
```
docker-compose up
```
To create superuser: check container id of offers_offers-django with:
```
docker ps
```
Then open shell in container with:
```
docker exec -it <container_id> /bin/sh
```
And finally create superuser with:
```
$ python manage.py createsuperuser
```


- Start with Python:

Preferably create a virtual environment.

cd to /Images
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.
```
pip install -r requirements.txt
```
With requirements installed you can run the app:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
To create superuser in Offers/offersproject:
```
python manage.py createsuperuser
```

# Tests
- With docker-compose:
Go into docker-compose.yml file, remove:
```
"python manage.py makemigrations &&
 python manage.py migrate &&
 python manage.py runserver 0:8000"
 ```
and put in pytest command:
 ```
 command: |
      sh -c "pytest"
 ```
next just cd to /Offers and use docker-compose by typing in console
 ```
 docker-compose up
 ```
- With python:

After installing app and requirements.txt simply go into /Offers/offersproject and type into console:
 
```
pytest
```
