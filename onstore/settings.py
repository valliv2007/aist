import os
# import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('my_secret_key', "שלום")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_COOKIE_SECURE = os.environ.get('my_csrf_cookie_secure') == 'True'
SESSION_COOKIE_SECURE = os.environ.get('my_session_cookie_secure') == 'True'
# X_FRAME_OPTIONS = os.environ.get('my_x_frame_options')
SECURE_BROWSER_XSS_FILTER = os.environ.get('my_secure_browser_xss_filter') == 'True'
SECURE_CONTENT_TYPE_NOSNIFF = os.environ.get('my_secure_content_type_nosniff') == 'True'
SECURE_SSL_REDIRECT = os.environ.get('my_secure_ssl_redirect') == 'True'
SECURE_HSTS_SECONDS = int(os.environ.get('my_hsts_seconds', 5))
SECURE_HSTS_PRELOAD = os.environ.get('my_secure_hsts_preload') == 'True'


ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'lenivastore.apps.LenivastoreConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'paypal.standard.ipn',
    'payment.apps.PaymentConfig',
    'cupons.apps.CuponsConfig',
    'users.apps.UsersConfig',
    'api.apps.ApiConfig',
    'crispy_forms',
    'phonenumber_field',
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'sslserver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'onstore.urls'

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
                'cart.context_processors.cart',
                'lenivastore.context_processors.categories_base',
            ],
        },
    },
]

WSGI_APPLICATION = 'onstore.wsgi.application'

if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
            'NAME': os.getenv('DB_NAME', 'postgres'),
            'USER': os.getenv('POSTGRES_USER', 'postgres'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'postgres'),
            'HOST': os.getenv('DB_HOST', 'database'),
            'PORT': os.getenv('DB_PORT', '5432')
        }
    }


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


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'  # 'UTC'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_THOUSAND_SEPARATOR = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CART_SESSION_ID = 'cart'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_BACKEND = os.environ.get('my_email_backend', 'django.core.mail.backends.filebased.EmailBackend')
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')
EMAIL_HOST = os.environ.get('my_email_host')
EMAIL_PORT = int(os.environ.get('my_email_port', 5225))
EMAIL_HOST_USER = os.environ.get('my_email_host_user')
EMAIL_HOST_PASSWORD = os.environ.get('my_email_host_password')
EMAIL_USE_TLS = os.environ.get('my_email_use_tls') == 'True'
EMAIL_USE_SSL = os.environ.get('my_email_use_ssl') == 'True'
DEFAULT_FROM_EMAIL = os.environ.get('my_email_host_user')
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

PAYPAL_RECEIVER_EMAIL = os.environ.get('my_email_host_user')
PAYPAL_TEST = True

AWS_ACCESS_KEY_ID = os.environ.get('my_aws_access_key_id')
AWS_SECRET_ACCESS_KEY = os.environ.get('my_aws_secret_access_key')
AWS_STORAGE_BUCKET_NAME = os.environ.get('my_aws_storage_bucket_name')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

AWS_S3_REGION_NAME = os.environ.get('my_aws_s3_region_name')
AWS_S3_SIGNATURE_VERSION = os.environ.get('my_aws_s3_signature_version')

# DEFAULT_FILE_STORAGE = os.environ.get('my_default_file_storage')

# django_heroku.settings(locals())
