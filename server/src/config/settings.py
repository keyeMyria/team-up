import os

import dotenv
from kombu import Exchange, Queue

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'accounts.User'

# Application definition

INSTALLED_APPS = [
    'jet',  # Must be before contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party apps
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
    'rest_framework',
    'channels',
    'django_filters',
    'rest_framework_swagger',
    'health_check',  # required
    'health_check.db',  # stock Django health checkers
    'health_check.cache',
    # 'health_check.storage',
    # 'health_check.contrib.celery',  # requires celery
    # 'health_check.contrib.s3boto_storage',
    'stdimage',
    # My apps
    'accounts.apps.AccountsConfig',
    'chatter.apps.ChatterConfig',
    'common.apps.CommonConfig',
    'games.apps.GamesConfig',
    'userprofiles.apps.UserprofilesConfig',
]

if DEBUG:
    INSTALLED_APPS += [
        'django_extensions',
        'debug_toolbar',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get('CACHE_LOCATION'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "KEY_PREFIX": "django_cache"
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/rest_framework/'

INTERNAL_IPS = ['*']

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'
LOGIN_REDIRECT_URL = 'documentation'

FORCE_SCRIPT_NAME = '/server'


# Rest framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'PAGE_SIZE': 20,  # Max number of results returned from a list API call
}

AUTHENTICATION_BACKENDS = (
    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    # Django
    'django.contrib.auth.backends.ModelBackend',
)

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')  # To be added
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')  # To be added

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from facebook.
# Email is not sent by default, to get it, you must request the email permission:
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

# Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'ROUTING': 'config.routing.channel_routing',
        'CONFIG': {
            'hosts': [(os.environ.get('REDIS_HOST'), int(os.environ.get('REDIS_PORT')))]
        }
    },
}

CHANNELS_API = {
    'DEFAULT_PERMISSION_CLASSES': ('channels_api.permissions.AllowAny',)
}

ASGI_APPLICATION = 'config.routing.application'

# CELERY
CELERY_TIMEZONE = TIME_ZONE

CELERY_BROKER_URL = 'amqp://{user}:{password}@{host}:{port}/{vhost}/'.format(
    user=os.environ.get('RABBIT_USER'),
    password=os.environ.get('RABBIT_PASS'),
    host=os.environ.get('RABBIT_HOST'),
    port=os.environ.get('RABBIT_PORT'),
    vhost=os.environ.get('RABBIT_ENV_VHOST', '')
)
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
BROKER_HEARTBEAT = '?heartbeat=30'
CELERY_BROKER_URL += BROKER_HEARTBEAT

# Redis
REDIS_PORT = int(os.environ.get('REDIS_PORT'))
REDIS_DB = 0
REDIS_HOST = os.environ.get('REDIS_HOST')

# Celery configuration

# configure queues, currently we have only one
CELERY_TASK_DEFAULT_QUEUE = 'default'
CELERY_TASK_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)

# Sensible settings for celery
# CELERY_TASK_ALWAYS_EAGER = False
# CELERY_TASK_ACKS_LATE = True
# CELERY_TASK_PUBLISH_RETRY = True
# CELERY_WORKER_DISABLE_RATE_LIMITS = False

# By default we will ignore result
# If you want to see results and try out tasks interactively, change it to False
# Or change this setting on tasks level
# CELERY_TASK_IGNORE_RESULT = True
# CELERY_RESULT_EXPIRES = 600

# Don't use pickle as serializer, json is much safer
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ['application/json']

# CELERY_WORKER_HIJACK_ROOT_LOGGER = False
# CELERY_WORKER_PREFETCH_MULTIPLIER = 1
# CELERY_WORKER_MAX_TASKS_PER_CHILD = 1000
