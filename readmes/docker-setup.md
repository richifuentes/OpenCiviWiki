## Prerequisites
The following packages are required to start developing CiviWiki:

- [Docker](https://docs.docker.com/install/)
- [Docker compose](https://docs.docker.com/compose/install/)

Below variables are also needed:

- [DJANGO SECRET KEY](https://www.miniwebtool.com/django-secret-key-generator/)
- [GOOGLE MAP KEY](https://developers.google.com/maps/documentation/javascript/get-api-key)

## Environment variables file
Execute below command:

    cp .env_sample .env
 
Then, fill `DJANGO_SECRET_KEY` and `GOOGLE_MAP_API_KEY` in `.env` file.


## Requirements
Execute docker command:

    docker-compose up

and that's it! Service should be available on address `0.0.0.0:8000`

Sometimes just running docker-compose up will not be enough, if you see issues with it then first run:

    docker-compose build

It could also be that you see the following messages when docker-compose build is running:
civiwiki-backend | You have 46 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): api, auth, contenttypes, notifications, sessions.
civiwiki-backend | Run 'python manage.py migrate' to apply them.

If you see the messages above then the application will not run and you will see lots of these messages:
ERROR:  relation "django_session" does not exist at character 109

If that is the case then you need to to run 'python manage.py migrate' to do that open a bash on the container running the web app:

    docker exec -it civiwiki-backend /bin/bash

then run:        
    cd project

and finally run:
    python manage.py migrate

## Log into docker console
Go to docker-shell to execute `./manage.py` commands by executing:

    docker exec -it civiwiki-backend /bin/bash

