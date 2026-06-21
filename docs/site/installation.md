# Installing the site

## Installing the prerequisites

```shell-session
$ apt update
$ apt install git gcc g++ make python3-dev python3-pip python3-venv libxml2-dev libxslt1-dev zlib1g-dev gettext curl redis-server pkg-config libpq-dev
```

Install Node.js 26 using nvm:

```shell-session
$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh | bash
$ source ~/.bashrc
$ nvm install 26
$ nvm use 26
$ node --version
```

## Creating the database

Next, we will set up the database using PostgreSQL. Install PostgreSQL if you haven't already.

```shell-session
$ apt update
$ apt install postgresql postgresql-client libpq-dev
```

The next step is to set up the database itself. You should execute the commands listed below to create the necessary database and user.

```shell-session
$ sudo -u postgres psql
postgres> CREATE USER freateoj WITH PASSWORD '<postgresql user password>';
postgres> CREATE DATABASE freateoj OWNER freateoj;
postgres> GRANT ALL PRIVILEGES ON DATABASE freateoj TO freateoj;
postgres> \q
```

## Installing prerequisites

Now that you are done, you can start installing the site. First, create a virtual environment and activate it. Here, we'll create a virtual environment named `freateojsite`.

```shell-session
$ python3 -m venv freateojsite
$ . freateojsite/bin/activate
```

You should see `(freateojsite)` prepended to your shell. Henceforth, `(freateojsite)` commands assume you are in the code directory, with the virtual environment active.

> **Note:** The virtual environment will help keep the modules needed separate from the system package manager, and save you many headaches when updating. Read more about virtual environments in the Python documentation.

Now, fetch the site source code:

```shell-session
(freateojsite) $ git clone --recursive https://github.com/freatevietnam/freateoj.git site
(freateojsite) $ cd site
```

Install Python dependencies into the virtual environment.

```shell-session
(freateojsite) $ pip3 install -r requirements.txt
```

Install Node.js packages:

```shell-session
(freateojsite) $ npm install
```

You will now need to configure `dmoj/local_settings.py`. You should make a copy of [this sample settings file](sample_files/local_settings.py) and read through it, making changes as necessary. Most importantly, you will want to update PostgreSQL credentials.

> **Note:** Leave debug mode on for now; we'll disable it later after we've verified that the site works.
>
> Generally, it's recommended that you add your settings in `dmoj/local_settings.py` rather than modifying `dmoj/settings.py` directly. `settings.py` will automatically read `local_settings.py` and load it, so write your configuration there.

## Compiling assets

FreateOJ uses `sass` and `autoprefixer` to generate the site stylesheets. FreateOJ comes with a `make_style.sh` script that may be run to compile and optimize the stylesheets.

```shell-session
(freateojsite) $ ./make_style.sh
```

Now, collect static files into `STATIC_ROOT` as specified in `dmoj/local_settings.py`.

```shell-session
(freateojsite) $ ./manage.py collectstatic
```

You will also need to generate internationalization files.

```shell-session
(freateojsite) $ ./manage.py compilemessages
(freateojsite) $ ./manage.py compilejsi18n
```

## Setting up Celery

The FreateOJ uses Celery workers to perform most of its heavy lifting, such as batch rescoring submissions. We will use Redis as its broker, though note that other brokers that Celery supports will work as well.

Start up the Redis server, which is needed by the Celery workers.

```shell-session
$ service redis-server start
```

Configure `local_settings.py` by uncommenting `CELERY_BROKER_URL` and `CELERY_RESULT_BACKEND`. By default, Redis listens on localhost port 6379, which is reflected in `local_settings.py`. You will need to update the addresses if you changed Redis's settings.

We will test that Celery works soon.

## Setting up database tables

We must generate the schema for the database, since it is currently empty.

```shell-session
(freateojsite) $ ./manage.py migrate
```

Next, load some initial data so that your install is not entirely blank.

```shell-session
(freateojsite) $ ./manage.py loaddata navbar
(freateojsite) $ ./manage.py loaddata language_small
(freateojsite) $ ./manage.py loaddata demo
```

> **Warning:** Keep in mind that the `demo` fixture creates a superuser account with a username and password of `admin`. If your
> site is exposed to others, you should change the user's password or remove the user entirely.

You should create an admin account with which to log in initially.

```shell-session
(freateojsite) $ ./manage.py createsuperuser
```

## Running the server

Now, you should verify that everything is going according to plan.

```shell-session
(freateojsite) $ ./manage.py check
```

At this point, you should attempt to run the server, and see if it all works.

```shell-session
(freateojsite) $ ./manage.py runserver 0.0.0.0:8000
```

You should Ctrl-C to exit after verifying.

> **Warning:** **Do not use `runserver` in production!**
>
> We will set up a proper webserver using nginx and uWSGI soon.

You should also test to see if `bridged` runs.

```shell-session
(freateojsite) $ ./manage.py runbridged
```

If there are no errors after about 10 seconds, it probably works.
You should Ctrl-C to exit.

Next, test that the Celery workers run.

```shell-session
(freateojsite) $ celery -A dmoj_celery worker
```

You can Ctrl-C to exit.

## Setting up uWSGI

`runserver` is insecure and not meant for production workloads, and should not be used beyond testing.
In the rest of this guide, we will be installing `uwsgi` and `nginx` to serve the site, using `supervisord`
to keep `site` and `bridged` running. It's likely other configurations may work, but they are unsupported.

First, copy our `uwsgi.ini` ([link](sample_files/uwsgi.ini)). You should change the paths to reflect your install.

You need to install `uwsgi`.

```shell-session
(freateojsite) $ pip3 install uwsgi
```

To test, run:

```shell-session
(freateojsite) $ uwsgi --ini uwsgi.ini
```

If it says workers are spawned, it probably works.
You should Ctrl-C to exit.

## Setting up supervisord

You should now install `supervisord` and configure it.

```shell-session
$ apt install supervisor
```

Copy our `site.conf` ([link](sample_files/site.conf)) to `/etc/supervisor/conf.d/site.conf`, `bridged.conf` ([link](sample_files/bridged.conf)) to `/etc/supervisor/conf.d/bridged.conf`, `celery.conf` ([link](sample_files/celery.conf)) to `/etc/supervisor/conf.d/celery.conf` and fill in the fields.

Next, reload `supervisord` and check that the site, bridged, and celery have started.

```shell-session
$ supervisorctl update
$ supervisorctl status
```

If all three processes are running, everything is good! Otherwise, peek at the logs and see what's wrong.

## Setting up nginx

Now, it's time to set up `nginx`.

```shell-session
$ apt install nginx
```

You should copy the sample `nginx.conf` ([link](sample_files/nginx.conf)), edit it and place it in wherever it is supposed to be for your nginx install.

> **Note:** Typically, `nginx` site files are located in `/etc/nginx/conf.d`.
> Some installations might place it at `/etc/nginx/sites-available` and require a symlink in `/etc/nginx/sites-enabled`.

Next, check if there are any issues with your nginx setup.

```shell-session
$ nginx -t
```

If not, reload the `nginx` configuration.

```shell-session
$ service nginx reload
```

You should be good to go. Visit the site at where you set it up to verify.

If it does not work, check `nginx` logs and `uwsgi` log `stdout`/`stderr` for details.

> **Note:** Now that your site is installed, remember to set `DEBUG` to `False` in `local_settings`. Leaving it `True` is a security risk.

## Configuration of event server

The event server uses Socket.IO for real-time updates. The daemon is a Node.js process that listens for HTTP POST requests from Django and broadcasts events to connected browser clients.

Configure in `local_settings.py`:

```python
EVENT_DAEMON_USE = True
EVENT_DAEMON_POST = 'http://localhost:9996/'  # Django posts events here
EVENT_DAEMON_GET = 'http://<your domain>/'    # Browser connects here (through nginx)
EVENT_DAEMON_POLL = '/channels/'              # Long-poll fallback path
```

Copy `wsevent.conf` ([link](sample_files/wsevent.conf)) to `/etc/supervisor/conf.d/wsevent.conf`, update the paths, then restart supervisor.

The Socket.IO daemon runs on a single port (default 9996) and handles:
- WebSocket/long-poll connections from browser clients
- HTTP POST requests from Django to broadcast events

```shell-session
$ supervisorctl update
$ supervisorctl restart bridged
$ supervisorctl restart site
$ service nginx restart
```
