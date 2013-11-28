# Django settings for project_management project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS


# set this to false to disable all automatic emails
PM_SEND_EMAILS = False

# set this false when celery is unavailable
PM_CELERY_AVAILABLE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/vagrant/dev.db',
    }
}


PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

PIPELINE_YUI_BINARY = "/usr/bin/env yui-compressor"

PIPELINE_CSS = {
    "bootstrap": {
        "source_filenames" : (
            "css/bootstrap.css",
        ),
        "output_filename": "css/bootstrap-min.css"
    },
    "tasks": {
        "source_filenames": (
            "tasks/css/common.css",
        ),
        "output_filename": "tasks/css/tasks.css"
    }
}


# Note: the two following settings are dev-instance only!
# do not use them on the production site, as they are
# slower/do not handle large data sets well.

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': '/vagrant/whoosh_index',
    }
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/vagrant/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/vagrant/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_STORAGE = "pipeline.storage.PipelineCachedStorage"

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@1-!_layba_#vieruhog9724piaes6&amp;%2cf9&amp;a-_%otld0e4#&amp;3ic&amp;^+oz1gt)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request"
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'project_management.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project_management.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'pipeline',
    'tasks',
    'widget_tweaks',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Email settings for project management emails
ADD_PROJECT_SUBJECT = "[Paly Robotics] A project has been created with you as lead"
EDIT_PROJECT_SUBJECT = "[Paly Robotics] A project you are leading has been updated"
ADD_TASK_AUTHOR_SUBJECT = "[Paly Robotics] You just authored a task"
ADD_TASK_ASSIGNED_SUBJECT = "[Paly Robotics] You have been assigned to a new task"
EDIT_TASK_AUTHOR_SUBJECT = "[Paly Robotics] A task you authored has been updated"
EDIT_TASK_ASSIGNED_SUBJECT = "[Paly Robotics] A task you are assigned to has been updated"

ADD_PROJECT_EMAIL = """Hello,
                            
    You've been added as lead on a new project. Make sure to check in with the
project manager and other captains as you make progress.

View project details at %s"""

EDIT_PROJECT_EMAIL = """Hello,

    A project you are loading has been updated. Check the project management site
for more details. Make sure to check in with the project manager and other captains
as you make progress.

View project details at %s"""

ADD_TASK_AUTHOR_EMAIL = """Hello,
    You just created task. Remember to keep tabs on its progress and
report to the project manager and other captains.

View task details at %s"""

ADD_TASK_ASSIGNED_EMAIL = """Hello,

    You've been assigned to a new task. Make sure to check in with the
project manager and other captains as you make progress.

View task details at %s"""

EDIT_TASK_AUTHOR_EMAIL = """Hello,
    A task you authored has been updated. Remember to keep tabs on its progress and
report to the project manager and other captains.

View task details at %s"""

EDIT_TASK_ASSIGNED_EMAIL = """Hello,

    A task you are assigned to has been updated. Make sure to check in with the
project manager and other captains as you make progress.

View task details at %s"""
