
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9)^nq$!vu(n#_vt!p5v&bgg_a@(8ok*$&mrb(h5@e1k9j4luf&'

# SECURITY WARNING: don't run with debug turned on in production!

#development
DEBUG = True
ALLOWED_HOSTS = []

#production
# DEBUG = False
# ALLOWED_HOSTS = ["api.ruthikegah.com", "www.api.ruthikegah.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    "home",
    'drf_yasg',
   "django.contrib.postgres",
    'django_editorjs',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Portfolio.urls'

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

WSGI_APPLICATION = 'Portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


#production
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ruth',
#         'USER': 'ruth',
#         'PASSWORD': 'ruth',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


##development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ruth',
        'USER': 'postgres',
        'PASSWORD': 'austinforreal',
        'PORT': '5432',
        'HOST': 'localhost'

    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# ##developments
STATIC_URL = '/static/'
STATICFILES_DIRS = [

    # os.path.join(BASE_DIR, 'static')

]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')





#production
# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, 'assets')
# ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
         'rest_framework.permissions.AllowAny',
    ]
}



CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
     "http://localhost:3001",
     "https://www.ruthikegah.com",
     "https://ruthikegah.com"


]


EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'contact@ruthikegah.com'
EMAIL_HOST_PASSWORD = 'Amezhiruth2'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = 'contact@ruthikegah.com'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]

}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'