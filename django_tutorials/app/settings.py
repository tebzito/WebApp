"""
Django settings for MusicStore project.
"""

#from django.conf.urls.static import static
from os import path
PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = (
  'localhost',
  )

ADMINS = (
     ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

STATIC_ROOT = "/var/www/static/"
STATIC_URL = "/static/"

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'app',
  #'rest_framework',
  ]

MIDDLEWARE_CLASSES = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  ]

LOGIN_URL = '/login'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'n(bd1f1c%e8=_xad02x5qtfn%wgwpi492e$8_erx+d)!tpeoim'

ROOT_URLCONF = 'app.urls'

TEMPLATE_DIRS = [path.join(PROJECT_ROOT, 'templates')]

'''
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [app/templates],
    'APPS_DIRS': True,
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
'''
WSGI_APPLICATION = 'app.wsgi.application'


DATABASES = {
  'default': {
    'ENGINE': 'mysql.connector.django',
    'NAME': 'music_app',
    'USER': 'bcc2f0e0f57d74',
    'PASSWORD': 'd273c06f',
    'HOST': 'br-cdbr-azure-south-b.cloudapp.net',
    'PORT': '',
  }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
  },
  {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
  },
  {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
  },
  {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
  },
]

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N =True

