"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from configurations import Configuration, values


class Commons(Configuration):
    """
       The common settings.
    """
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = values.ListValue([], separator=';')

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'django_extensions',
        'webpack_loader',
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

    ROOT_URLCONF = '{{ project_name }}.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    )

    # Password validation
    # https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/2.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.2/howto/static-files/

    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'assets'),
    )
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    WHITENOISE_ENABLED = values.BooleanValue(False, environ_name='WHITENOISE_ENABLED')

    if WHITENOISE_ENABLED:
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
        INSTALLED_APPS = INSTALLED_APPS + [
            'whitenoise.runserver_nostatic',
        ]
        MIDDLEWARE = MIDDLEWARE + [
            'whitenoise.middleware.WhiteNoiseMiddleware',
        ]


class Development(Commons):
    """
       The in-development settings.
    """
    DEBUG = True
    # If using inside docker container, please make sure add docker0 interface ip, the usual is 172.17.0.1 (in my case)
    INTERNAL_IPS = [
        '127.0.0.1',
        '172.17.0.1'
    ]
    INSTALLED_APPS = Commons.INSTALLED_APPS + [
        'debug_toolbar',
    ]
    MIDDLEWARE = Commons.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    WEBPACK_LOADER = {
        'DEFAULT': {
            'CACHE': False,
            'BUNDLE_DIR_NAME': 'bundle/',  # must end with slash
            'STATS_FILE': os.path.join(Commons.BASE_DIR, 'webpack-stats.json'),
            'POLL_INTERVAL': 0.1,
            'TIMEOUT': None,
        }
    }


class Staging(Commons):
    """
       The in-staging or testing, or low to medium load settings.
    """
    SESSION_COOKIE_SECURE = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    WEBPACK_LOADER = {
        'DEFAULT': {
            'CACHE': False,
            'BUNDLE_DIR_NAME': 'bundle/',  # must end with slash
            'STATS_FILE': os.path.join(Commons.BASE_DIR, 'webpack-stats.json'),
            'POLL_INTERVAL': 0.1,
            'TIMEOUT': None,
        }
    }


class Production(Commons):
    """
        The in-production settings.
    """
    SESSION_COOKIE_SECURE = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    WEBPACK_LOADER = {
        'DEFAULT': {
            'CACHE': True,
            'BUNDLE_DIR_NAME': 'bundle/',  # must end with slash
            'STATS_FILE': os.path.join(Commons.BASE_DIR, 'webpack-stats.json'),
            'POLL_INTERVAL': 0.1,
            'TIMEOUT': None,
            'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
        }
    }
