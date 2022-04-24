# analytics-backend

**Note: This repository has been superseded by [Dymaxion Labs Platform](https://github.com/dymaxionlabs/platform).**

[![Build Status](https://travis-ci.org/dymaxionlabs/analytics-backend.svg?branch=master)](https://travis-ci.org/dymaxionlabs/analytics-backend)
[![codecov](https://codecov.io/gh/dymaxionlabs/analytics-backend/branch/master/graph/badge.svg)](https://codecov.io/gh/dymaxionlabs/analytics-backend)

Dymaxion Analytics backend repository.

For more information on the frontend, see the repository at
[https://github.com/dymaxionlabs/analytics-frontend](https://github.com/dymaxionlabs/analytics-frontend).

## Requirements

* Python 3
* PostgreSQL 9.4+ with PostGIS 2 extension
* GDAL, Proj, etc.

## Development

* Install dependencies

```
sudo apt-get install \
  libgdal-dev \
  libproj-dev \
  postgis \
  postgresql \
  python3 \
  python3-dev \
  python3-pip
```

* Create a role and database (e.g. `terra`)

```
sudo -u postgres createuser --interactive
sudo -u postgres createdb terra
```

* Set user password for Django

```
$ psql terra
# ALTER USER terra WITH PASSWORD 'foobar';
```

* Copy `env.sample` and edit it to suit your needs. You will have to set
  `DB_USER`, `DB_PASS` and `DB_NAME`.

```
cp env.sample .env
```

* Install Python dependencies using Pipenv. Install it first if you don't have it:

```
pip install --user -U pipenv
pipenv install
pipenv install \
  django-anymail[mailgun] \
  django-rest-auth[with_social] \
  django-storages[google]
```

Then inside a pipenv shell (use `pipenv shell`) you should first do the following:

* Run migrations: `./manage.py migrate`
* Create superuser: `./manage.py createsuperuser`

Now you can:

* Run server: `./manage.py runserver`
* Run tests: `./manage.py test`

When deploying for the first time:

* Set `DEBUG=0` and `ALLOWED_HOSTS` list with domains/subdomains and IPs
* Also, set a long unique `SECRET_KEY`
* Collect statics with `./manage.py collectstatic`

### Async tasks

We use Celery for asynchronous tasks like preprocessing and prediction tasks.
Redis is the current broker backend.

* Run a worker

```
celery -A terra worker -l info
```

* Start Flower monitoring app.

```
celery -A terra flower
```

Then, visit http://localhost:5555

### Honcho

You can use [Honcho](https://honcho.readthedocs.io) to fire up everything (web
server, workers and Flower) on your dev machine. Simple run `honcho start`.
You can also start specific processes: `honcho start web`, `honcho start
worker`, etc.

See [Procfile](Procfile).

### Translations

When adding new translated strings:

* Run `django-admin makemessages`
* Update .po files
* Run `django-admin compilemessages`

## Issue tracker

Please report any bugs and enhancement ideas using the GitHub issue tracker:

  https://github.com/dymaxionlabs/analytics-backend/issues


## Help wanted

Any help in testing, development, documentation and other tasks is highly
appreciated and useful to the project.

For more details, see the file [CONTRIBUTING.md](CONTRIBUTING.md).


## License

Source code is released under a BSD-2 license.  Please refer to
[LICENSE.md](LICENSE.md) for more information.
