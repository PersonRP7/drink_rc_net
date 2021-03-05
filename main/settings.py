"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# from braintree import Configuration, Environment
import data

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = data.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Previous version
# ALLOWED_HOSTS = ["kavashop.pythonanywhere.com"]
# ALLOWED_HOSTS = ["www.prometaroma.net"]
# ALLOWED_HOSTS = ["www.prometaroma.hr"]
ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'users.apps.UsersConfig',
    'about.apps.AboutConfig',
    'products.apps.ProductsConfig',
    # Added search module below
    'search_module',
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

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
# 'default': {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': 'kavashop$db',
#     'USER': 'kavashop',
#     'PASSWORD': 'kvshp678xyz!',
#     'HOST': 'kavashop.mysql.pythonanywhere-services.com',
# }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
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

TIME_ZONE = 'Europe/Zagreb'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = '/home/kavashop/drink_rc/static'

# STATICFILES_DIRS = [
#     BASE_DIR / "static"
# ]

# Media files
MEDIA_ROOT = '/home/kavashop/drink_rc/media/'
MEDIA_URL = '/media/'

# Login settings
LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'users:userprofile_redirect'

# Crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Custom User Model
AUTH_USER_MODEL = 'users.CustomUser'

# Email settings
# EMAIL_HOST = os.getenv("EMAIL_HOST")
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = os.getenv("EMAIL_PORT")
# EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")

# Braintree settings
BT_ENVIRONMENT = data.BT_ENVIRONMENT
BT_MERCHANT_ID = data.BT_MERCHANT_ID
BT_PUBLIC_KEY = data.BT_PUBLIC_KEY
BT_PRIVATE_KEY = data.BT_PUBLIC_KEY

# Configuration.configure(
#     Environment.Sandbox,
#     BT_MERCHANT_ID,
#     BT_PUBLIC_KEY,
#     BT_PRIVATE_KEY
# )

# Snipcart settings
DATA_API_KEY=data.DATA_API_KEY