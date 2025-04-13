"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
import logging

from pathlib import Path



logger = logging.getLogger('django')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-=mk1vs1e$7)c(ng!8)u@yd@pu1a!ccrkdo7nx%(ky0ka3@&myz"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "news.apps.NewsConfig",
    "accounts",
    'django_filters',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",


    
]

ROOT_URLCONF = "NewsPaper.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = "NewsPaper.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_DIRS = [BASE_DIR / 'static']

LOGIN_URL = '/accounts/login/' 

LOGIN_REDIRECT_URL = '/news'


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {'signup': 'accounts.models.BasicSignupForm'}


## wsmktdvjzucabegt

#EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
##EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
#EMAIL_HOST_USER = 'vdovin.tema'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
#EMAIL_HOST_PASSWORD = 'Dfcbkbcf518'  # пароль от почты
#EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но включать его здесь обязательно
#DEFAULT_FROM_EMAIL = "vdovin.tema@yandex.ru"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "vdovin.tema@yandex.ru"
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "vdovin.tema@yandex.ru"

SERVER_EMAIL = "vdovin.tema@yandex.ru"

SITE_URL ='http://127.0.0.1:8000'

# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам) 
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
 
# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style' : '{', 
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': "%d.%m.%Y %H-%M-%S"
        },
        'simple_wrg':{
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
            'datefmt': "%d.%m.%Y %H-%M-%S"
        },
        'simple_err':{
            'format': '%(asctime)s %(levelname)s %(message)s %(exc_info)s',
            'datefmt': "%d.%m.%Y %H-%M-%S"    
        },
        'general_log':{
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s ',
            'datefmt': "%d.%m.%Y %H-%M-%S" 
        },
        'errors_log':{
            'format': '%(asctime)s %(levelname)s %(pathname)s %(exc_info)s %(message)s ',
            'datefmt': "%d.%m.%Y %H-%M-%S" 
        },
        'security_log':{
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s ',
            'datefmt': "%d.%m.%Y %H-%M-%S"  
        },
        'email_log':{
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s ',
            'datefmt': "%d.%m.%Y %H-%M-%S" 
        }
        
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    }, 
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_wrg': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter':'simple_wrg'
        },
        'console_err': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter':'simple_err'
        },
        'general_log':{
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'logs/general.log',
            'formatter':'general_log'
        },
        'errors_log':{
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
            'formatter':'errors_log'
        },
        'security_log':{
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/securitylog',
            'formatter':'security_log'
        },
        'email':{
            'level':'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'email_log'
        }

        
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_wrg', 'console_err', 'general_log'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors_log', 'email'],
            'propagate': True,
        },
        'django.server':{
            'handlers': ['errors_log', 'email'],
            'propagate': True,    
        },
        'django.template':{
            'handlers': ['errors_log'],
            'propagate': True,
        },
        'django.db.backends':{
            'handlers': ['errors_log'],
            'propagate': True,
        },
        'django.security':{
            'handlers': ['security_log'],
            'propagate': True,
        }

    }
}