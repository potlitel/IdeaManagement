"""
Django settings for IdeaManagement project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p$j%s$bs3l4e42sbl&+7w41j8^f3v^q&m7gb1cr35js896=8fh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

RECAPTCHA_PUBLIC_KEY = '76wtgdfsjhsydt7r5FFGFhgsdfytd656sad75fgh'
RECAPTCHA_PRIVATE_KEY = '98dfg6df7g56df6gdfgdfg65JHJH656565GFGFGs'
NOCAPTCHA = False

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_comments',
    'richcomments',
    'IdeaPublisher',
    'simplemathcaptcha',
    #'djangoratings',
	'crispy_forms',
	'fm',
    'django_messages',
    #'ratings'
    'secretballot',
	'pure_pagination',
    'likes',
    'avatar',
    #'pagination',
    'django_password_strength',
)

PAGINATION_SETTINGS = {
        'PAGE_RANGE_DISPLAYED': 10,
        'MARGIN_PAGES_DISPLAYED': 2,

        'SHOW_FIRST_PAGE_WHEN_INVALID': True,
    }

COMMENTS_APP = 'richcomments'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'likes.middleware.SecretBallotUserIpUseragentMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'IdeaManagement.urls'

WSGI_APPLICATION = 'IdeaManagement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticFilesLocation')
#STATIC_URL = os.path.join(BASE_DIR, '/static/')
STATICFILES_DIRS = (
            os.path.join(BASE_DIR, "static"), 
            os.path.join(BASE_DIR, "IdeaPublisher/static"), 
    )

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'templates/likes/templates/likes/inclusion_tags'),
)

# AUTH_USER_MODEL = 'myauth.User'

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages",
                               'django_messages.context_processors.inbox',)


# URL of the login page.
LOGIN_URL = '/login/'
# The URL where requests are redirected after login when the contrib.auth.login
# view gets no next parameter.
LOGIN_REDIRECT_URL = '/IdeaPublisher/'

SITE_ID = 1