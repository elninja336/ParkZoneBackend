import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR


ALLOWED_HOSTS =[os.environ['WEBSITE_HOSTNAME']]
CRS_TRUSTED_ORIGIN =['https://'+os.environ['WEBSITE_HOSTNAME']]

DEBUG = False

SECRET_KEY = os.environ.get['SECRET_KEY']

# Security setting for production
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [ ]
#     "http://localhost:3000",  # my frontend URL
# ]