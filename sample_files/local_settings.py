#####################################
########## Django settings ##########
#####################################
# See Django documentation
# for more info and help. If you are stuck, you can try Googling about
# Django - many of these settings below have external documentation about them.
#
# The settings listed here are of special interest in configuring the site.

# SECURITY WARNING: keep the secret key used in production secret!
# You may use this command to generate a key:
# python3 -c 'from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())'
SECRET_KEY = 'This key is not very secure and you should change it.'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Change to False once you are done with runserver testing.

# Uncomment and set to the domain names this site is intended to serve.
# You must do this once you set DEBUG to False.
#ALLOWED_HOSTS = ['oj.freate.io.vn']

# Optional apps that DMOJ can make use of.
INSTALLED_APPS += (
)

# Caching. You can use memcached or redis instead.
# Documentation: See Django documentation
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

# Your database credentials. PostgreSQL is required.
# Documentation: See Django documentation
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dmoj',
        'USER': 'dmoj',
        'PASSWORD': '<postgresql user password>',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    },
}

# Sessions.
# Documentation: See Django documentation
#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Internationalization.
# Documentation: See Django documentation
LANGUAGE_CODE = 'vi'
DEFAULT_USER_TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

## django-compressor settings, for speeding up page load times by minifying CSS and JavaScript files.
# Documentation: See django-compressor documentation
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)


#########################################
########## Email configuration ##########
#########################################
# See Django documentation
# for more documentation. You should follow the information there to define
# your email settings.

# Use this if you are just testing.
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# The following block is included for your convenience, if you want
# to use Gmail.
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = '<your account>@gmail.com'
#EMAIL_HOST_PASSWORD = '<your password>'
#EMAIL_PORT = 587

# To use Mailgun, uncomment this block.
# You will need to run `pip install django-mailgun-mime` to get `MailgunBackend`.
#EMAIL_BACKEND = 'django_mailgun_mime.backends.MailgunMIMEBackend'
#MAILGUN_API_KEY = '<your Mailgun access key>'
#MAILGUN_DOMAIN_NAME = '<your Mailgun domain>'

# You can also use SendGrid, with `pip install sendgrid-django`.
#EMAIL_BACKEND = 'sgbackend.SendGridBackend'
#SENDGRID_API_KEY = '<Your SendGrid API Key>'

# The DMOJ site is able to notify administrators of errors via email,
# if configured as shown below.

# A tuple of (name, email) pairs that specifies those who will be mailed
# when the server experiences an error when DEBUG = False.
ADMINS = (
    ('Your Name', 'freatevietnam@gmail.com'),
)

# The sender for the aforementioned emails.
SERVER_EMAIL = 'FreateOJ: Freate Online Judge <freateoj@freate.io.vn>'


################################################
########## Static files configuration ##########
################################################
# See Django documentation.

# Change this to somewhere more permanent, especially if you are using a
# webserver to serve the static files. This is the directory where all the
# static files DMOJ uses will be collected to.
# You must configure your webserver to serve this directory as /static/ in production.
STATIC_ROOT = '/tmp/static'

# URL to access static files.
#STATIC_URL = '/static/'

# Uncomment to use hashed filenames with the cache framework.
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


############################################
########## DMOJ-specific settings ##########
############################################

## DMOJ site display settings.
SITE_NAME = 'FreateOJ'
SITE_FULL_URL = 'https://oj.freate.io.vn'
SITE_LONG_NAME = 'FreateOJ: Freate Online Judge'
SITE_ADMIN_EMAIL = 'freatevietnam@gmail.com'
TERMS_OF_SERVICE_URL = '//oj.freate.io.vn/tos/'  # Use a flatpage.

## Media files settings.
# This is the directory where all the media files are stored.
# Change this to somewhere more permanent.
# You must configure your webserver to serve this directory in production.
MEDIA_ROOT = '/tmp/media'

## Problem data settings.
# This is the directory where all the problem data are stored.
# Change this to somewhere more permanent.
FREATEOJ_PROBLEM_DATA_ROOT = '/tmp/problem_data/'

## Bridge controls.
# The judge connection address and port; where the judges will connect to the site.
# You should change this to something your judges can actually connect to
# (e.g., a port that is unused and unblocked by a firewall).
BRIDGED_JUDGE_ADDRESS = [('localhost', 9999)]

# The bridged daemon bind address and port to communicate with the site.
#BRIDGED_DJANGO_ADDRESS = [('localhost', 9998)]

## DMOJ features.
# Set to True to enable full-text searching for problems.
ENABLE_FTS = False

# Set of email providers to ban when a user registers, e.g., {'throwawaymail.com'}.
BAD_MAIL_PROVIDERS = set()

# The number of submissions that a staff user can rejudge at once without
# requiring the permission 'Rejudge a lot of submissions'.
# Uncomment to change the submission limit.
#FREATEOJ_SUBMISSIONS_REJUDGE_LIMIT = 10

## Event server.
# Uncomment to enable live updating.
#EVENT_DAEMON_USE = True

# Socket.IO event daemon HTTP POST URL (for Django to send events to the daemon)
#EVENT_DAEMON_POST = 'http://localhost:9996/'

# Public URL for clients to connect to the Socket.IO server (through nginx reverse proxy)
#EVENT_DAEMON_GET = 'http://<your domain>/'
#EVENT_DAEMON_GET_SSL = 'https://<your domain>/'
#EVENT_DAEMON_POLL = '/channels/'

# If you would like to use the AMQP-based event server from See event-server documentation,
# uncomment this section instead. This is more involved, and recommended to be done
# only after you have a working event server.
#EVENT_DAEMON_AMQP = '<amqp:// URL to connect to, including username and password>'
#EVENT_DAEMON_AMQP_EXCHANGE = '<AMQP exchange to use>'

## Celery
#CELERY_BROKER_URL = 'redis://localhost:6379'
#CELERY_RESULT_BACKEND = 'redis://localhost:6379'

## CDN control.
# Base URL for a copy of Ace editor.
# Should contain ace.js, along with mode-*.js.
ACE_URL = '//cdnjs.cloudflare.com/ajax/libs/ace/1.2.3/'
JQUERY_JS = '//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js'
SELECT2_JS_URL = '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js'
SELECT2_CSS_URL = '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css'

# A map of Earth in equirectangular projection, for timezone selection.
# Please try not to hotlink this poor site.
TIMEZONE_MAP = '<URL to a world map image>'

## Camo (See Camo documentation) usage.
#FREATEOJ_CAMO_URL = '<URL to your camo install>'
#FREATEOJ_CAMO_KEY = '<The CAMO_KEY environmental variable you used>'

# Domains to exclude from being camo'd.
#FREATEOJ_CAMO_EXCLUDE = ('https://oj.freate.io.vn',)

# Set to True to use https when dealing with protocol-relative URLs.
# See protocol-relative URL documentation for what they are.
#FREATEOJ_CAMO_HTTPS = False

# HTTPS level. Affects <link rel='canonical'> elements generated.
# Set to 0 to make http URLs canonical.
# Set to 1 to make the currently used protocol canonical.
# Set to 2 to make https URLs canonical.
#FREATEOJ_HTTPS = 0

## PDF rendering settings.

# Enable PDF generation.
#FREATEOJ_PDF_PDFOID_URL = '<URL to your pdfoid install>.'

# Directory to cache the PDF.
#FREATEOJ_PDF_PROBLEM_CACHE = '/home/dmoj-uwsgi/pdfcache'

# Path to use for nginx's X-Accel-Redirect feature.
# Should be an internal location mapped to the above directory.
#FREATEOJ_PDF_PROBLEM_INTERNAL = '/pdfcache'

## Data download settings.
# Uncomment to allow users to download their data.
#FREATEOJ_USER_DATA_DOWNLOAD = True

# Directory to cache user data downloads.
# It is the administrator's responsibility to clean up old files.
#FREATEOJ_USER_DATA_CACHE = '/home/dmoj-uwsgi/userdatacache'

# Path to use for nginx's X-Accel-Redirect feature.
# Should be an internal location mapped to the above directory.
#FREATEOJ_USER_DATA_INTERNAL = '/userdatacache'

# How often a user can download their data.
#FREATEOJ_USER_DATA_DOWNLOAD_RATELIMIT = datetime.timedelta(days=1)

# Uncomment to allow contest authors to download contest data
#FREATEOJ_CONTEST_DATA_DOWNLOAD = True

# Directory to cache contest data downloads.
# It is the administrator's responsibility to clean up old files.
#FREATEOJ_CONTEST_DATA_CACHE = '/home/dmoj-uwsgi/contestdatacache'

# Path to use for nginx's X-Accel-Redirect feature.
# Should be an internal location mapped to the above directory.
#FREATEOJ_CONTEST_DATA_INTERNAL = '/contestdatacache'

# How often contest data can be exported.
# This applies per contest, not per user.
#FREATEOJ_CONTEST_DATA_DOWNLOAD_RATELIMIT = datetime.timedelta(days=1)

## ======== Logging Settings ========
# Documentation: See Django documentation
#                See Python logging documentation
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        # You may use this handler as an example for logging to other files.
        'bridge': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '<desired bridge log path>',
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'file',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'dmoj.throttle_mail.ThrottledEmailHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'file',
        },
    },
    'loggers': {
        # Site 500 error mails.
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Judging logs as received by bridged.
        'judge.bridge': {
            'handlers': ['bridge', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        # Catch all logs to stderr.
        '': {
            'handlers': ['console'],
        },
        # Other loggers of interest. Configure at will.
        #  - judge.user: logs naughty user behaviours.
        #  - judge.problem.pdf: PDF generation log.
        #  - judge.html: HTML parsing errors when processing problem statements etc.
        #  - judge.mail.activate: logs for the reply to activate feature.
        #  - event_socket_server
    },
}

## ======== Integration Settings ========
## Python Social Auth
# Documentation: See python-social-auth documentation
# You can define these to enable authentication through the following services.
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
#SOCIAL_AUTH_FACEBOOK_KEY = ''
#SOCIAL_AUTH_FACEBOOK_SECRET = ''
#SOCIAL_AUTH_GITHUB_SECURE_KEY = ''
#SOCIAL_AUTH_GITHUB_SECURE_SECRET = ''

## ======== Custom Configuration ========
# You may add whatever Django configuration you would like here.
# Do try to keep it separate so you can quickly patch in new settings.
