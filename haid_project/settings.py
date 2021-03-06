"""
Django settings for haid_project project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env(".env")


def env_to_bool(val, default):
    str_val = env(val)
    return default if str_val is None else str_val == 'True'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'enq+87g#0$en!ro0xp!00p#=vr)uj^-h5wc**!mkenduiqjejv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"];

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'corsheaders',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    'haid_project',
    'accounts',
    'organization',
    'project',
    'oauth',
    'notification'
]

AUTH_USER_MODEL = "accounts.HaidUser"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'haid_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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
# swagger ?????????
SWAGGER_SETTINGS = {
    # ????????????
    # 'SECURITY_DEFINITIONS': {
    #     "basic": {
    #         'type': 'basic'
    #     }
    # },
    # ?????????????????????????????????????????????, ?????????????????????restframework?????????.
    # 'LOGIN_URL': 'rest_framework:login',
    # 'LOGOUT_URL': 'rest_framework:logout',
    # 'DOC_EXPANSION': None,
    # 'SHOW_REQUEST_HEADERS':True,
    # 'USE_SESSION_AUTH': True,
    # 'DOC_EXPANSION': 'list',
    # ???????????????????????????????????????????????????
    'APIS_SORTER': 'alpha',
    # ????????????json??????, ????????????????????????json?????????
    'JSON_EDITOR': True,
    # ????????????????????????
    'OPERATIONS_SORTER': 'alpha',
    'VALIDATOR_URL': None,
}
REST_FRAMEWORK = {
    # ??????????????????coreapi???Schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}
WSGI_APPLICATION = 'haid_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        # python????????????????????????????????????????????????
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # ??????????????????????????????????????????
        'ENGINE': 'django.db.backends.mysql',  # ???????????????
        'NAME': 'haid',  # ???????????????
        'USER': 'root',  # ??????????????????????????????
        'PASSWORD': 'codemao',  # ????????????
        'HOST':  '127.0.0.1', #'mysql_haid',  # ??????????????????????????????ip??????
        'PORT': '3308',  # ??????mysql????????????
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATICFILES_DIRS = [
#             os.path.join(BASE_DIR, "static/"),
# 			]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# STATIC_URL = '/static/static/'
# MEDIA_URL = '/static/media/'
print(env.str("DJANGO_EMAIL_TLS"))
# Email:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = env.bool('DJANGO_EMAIL_TLS', False)
EMAIL_USE_SSL = env.bool('DJANGO_EMAIL_SSL', True)
EMAIL_HOST = env('DJANGO_EMAIL_HOST') or 'smtp.mxhichina.com'
EMAIL_PORT = int(env('DJANGO_EMAIL_PORT') or 465)
EMAIL_HOST_USER = env('DJANGO_EMAIL_USER')
EMAIL_HOST_PASSWORD = env.str('DJANGO_EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# redis:
REDIS_PASSWORD = env('DJANGO_REDIS_PASSWORD')
CACHES = {
    'default': {
        'BACKEND': "django_redis.cache.RedisCache",
        'LOCATION': "redis://" + 'redis_haid',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "PASSWORD": REDIS_PASSWORD}

    }
}
# print("test")
# print(CACHES)
# print("test")
# print(EMAIL_HOST_PASSWORD)

REDIS_EXPIRE_TIME_EMAIL_VERIFICATION_CODE = 3000
REGISTER_CACHE_KEY = 'HAID:EMAIL:VERIFICATION:'

# cors ??????
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
#CORS_ORIGIN_WHITELIST = ('*')

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
