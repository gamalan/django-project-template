# Django 2.0+ project template

This is a simple Django 2.0+ project template with my preferred setup. Based on https://github.com/jpadilla/django-project-template

## Features

- Django 2.0+
- Uses [Pipenv](https://github.com/kennethreitz/pipenv) - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Webpack loader, with different config for different needs
- Dockerfile example, deploy with gunicorn with or without nginx, monitored using supervisord
- Use Whitenoise if not using nginx, can be enabled through `DJANGO_WHITENOISE_ENABLED` environment variable
- Bulma CSS Framework
- [StimulusJS](https://stimulusjs.org/)

## How to install

```bash
$ django-admin.py startproject \
  --template=https://github.com/gamalan/django-project-template/archive/master.zip \
  --name=mysite \
  --extension=py,md,env,json \
  project_name
$ mv example.env .env
$ pipenv install --dev
```

## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```
ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY='dont-tell-eve'
DJANGO_DEBUG='yes'
```

These settings(and their default values) are only used on staging and production environments.

```
DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=''
DJANGO_SECURE_SSL_HOST=''
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'
```

## Deployment

Whatever floats your boats.
Available deployment option:

- Docker Image
- Manual deployment
- Heroku

## Note

- If you see the supervisord configuration, `PIPENV_DONT_LOAD_ENV="true"` this part is so pipenv don't read .env first, because it will mess with passed environment variable.