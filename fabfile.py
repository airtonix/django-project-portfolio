from __future__ import with_statement

import re
import os, sys
import jinja2

from fabric import colors
from fabric.api import (local, run, sudo, abort, cd, lcd,
                        prefix, parallel, settings, hide,
                        puts, execute, roles)

from fabric.decorators import task
from fabric.operations import get, prompt
from fabric.contrib import files
from fabric.contrib.files import append, comment
from fabric.contrib.console import confirm

import fabtools
from functools import wraps
from contextlib import contextmanager as _contextmanager

from django.conf import settings
from django.test.simple import run_tests


HERE_DIR = os.path.abspath(os.path.dirname(__file__))
TEST_DIR = os.path.join(HERE_DIR, "testing_temp")

@task
def test():
    local("mkdir {}".format(TEST_DIR))

    settings.configure(DEBUG = True,
                       DATABASE_ENGINE = 'sqlite3',
                       DATABASE_NAME = os.path.join(TEST_DIR, 'database.db'),
                       INSTALLED_APPS = ('django.contrib.auth',
                                         'django.contrib.contenttypes',
                                         'django.contrib.sessions',
                                         'django.contrib.admin',
                                         'projects',
                                         'projects.tests',))

    failures = run_tests(['projects',], verbosity=1)
    if failures:
        sys.exit(failures)