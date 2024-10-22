"""
Django settings for myapp_allauth_users project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zirvah7@u$203$h694xt*uynjdnga9=(hy5obdhdy3_4c72jla'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dms-allauth-demo.herokuapp.com','127.0.0.1','localhost',
                 '127.0.0.1:8000','*']


# Application definition

INSTALLED_APPS = [
    'channels',
    'chat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',

    'allauth',
    'django.contrib.sites',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.bitbucket',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'allauth_registration',



]

SITE_ID=1
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_FORMS = {
    'signup': 'allauth_registration.forms.CustomSignupForm',


}
ACCOUNT_LOGIN_ATTEMPTS_LIMIT=100

LOGIN_REDIRECT_URL='home'
#LOGOUT_REDIRECT_URL='account_login'

ACCOUNT_LOGOUT_REDIRECT_URL ='account_login'

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS=True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE=False
ACCOUNT_LOGIN_ON_PASSWORD_RESET=True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION=True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=1    # 1 day
ACCOUNT_UNIQUE_EMAIL=True
SOCIALACCOUNT_AUTO_SIGNUP=False
AUTHENTICATION_BACKENDS=[
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'django.contrib.auth.backends.AllowAllUsersRemoteUserBackend',
]
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30 # One month (defined in seconds)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'myapp_allauth_users.urls'
ASGI_APPLICATION = 'myapp_allauth_users.routing.application'
CHANNEL_LAYERS={
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1',6379)],
            # "hosts": [('redis://:b9u7JRrvqsC05uMvXxnCHNEYA4w08iqH@redis-10616.c82.us-east-1-2.ec2.cloud.redislabs.com:10616')],
        },
    },
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
            os.path.join(BASE_DIR, 'templates', 'allauth_registration'),


        ],
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

# WSGI_APPLICATION = 'myapp_allauth_users.wsgi.application'
###################################################################
# ASGI_APPLICATION = 'myapp_allauth_users.routing.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {'default': dj_database_url.config(default='postgres://musnkcilwpwbbl:5c2ddeed6ca255fae1c6b03960bb02ff393fe0312e1401eed4a2b3c9278759de@ec2-174-129-18-247.compute-1.amazonaws.com:5432/d54s57v1g84i5s')}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_DIR = os.path.join(BASE_DIR,'static')

STATICFILES_STORAGE ='django.contrib.staticfiles.storage.StaticFilesStorage'

STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)
STATICFILES_DIRS = (
    STATIC_DIR,
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



CRISPY_TEMPLATE_PACK = 'bootstrap4'

#EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # mail service smtp
EMAIL_HOST_USER = 'dms24081999@gmail.com' # email id
EMAIL_HOST_PASSWORD = 'fsawkexebivuyccd' #password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
