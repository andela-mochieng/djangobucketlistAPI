"""
Test specific settings.
"""

from .base import *

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
SECRET_KEY = " Your my test secret"

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=bucketlist,api',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testdb',
    }
}
