# My Little Office

## Requirements

To deploy app, you need [`docker`](https://docs.docker.com/engine/install/) and `docker-compose`.

## Instalation

1. Clone this repo to local machine.

2. Change directory.

`cd ./my-little-office`

3. Start app.

`docker-compose up -d`

4. Optionaly, add superuser to maintain data.

`docker-compose run django python manage.py createsuperuser`

5. Enjoy. Go to the `localhost:8000`

## Features

* API can be accessed by `/api/`

    * There are helpful schema: `/api/swagger-ui/`

    * List of all users: `/api/staff/`

    * List of all users by level: `/api/staff/?level={level}`

    * View of user profile: `/api/self/`

    This view can bee accessed only y token. Obtain it at `/api/token/`. Then, add to headers `Authorization: Token {token}`

* To use API of staff, user must have a `Staff | Employee | Can view API`

* Seed DB by prompt command `docker-compose run django python manage.py seed [--posititon=15 --staff_l0=1 --staff_l1=5 --staff_l2=10 --staff_l3=15  --staff_l4=50 ]`


