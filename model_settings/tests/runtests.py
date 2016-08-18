#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import sys

import coverage
import django
from django.conf import settings
from django.core.management import execute_from_command_line

logger = logging.getLogger(__name__)
ch = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(ch)
logger.setLevel(logging.INFO)

CURRENT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "../.."))
sys.path.insert(0, os.path.abspath(BASE_DIR))
coverage_conf = os.path.join(CURRENT_DIR, "coverage.conf")

cov = coverage.coverage(
    cover_pylib=False,
    config_file=coverage_conf,
    include="{0}/*".format(BASE_DIR)
)
cov.start()

INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "polymorphic",
    "model_settings"
)

settings.configure(
    SECRET_KEY="tests_secret_key",
    DEBUG=False,
    TEMPLATE_DEBUG=False,
    ALLOWED_HOSTS=[],
    INSTALLED_APPS=INSTALLED_APPS,
    MIDDLEWARE_CLASSES=[],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    LANGUAGE_CODE="en-US",
    TIME_ZONE="UTC",
    USE_I18N=False,
    USE_L10N=False,
    USE_TZ=True,
)

try:
    django.setup()
except AttributeError:
    pass


def main():
    argv = [sys.argv[0], "test"]
    argv.append(".")
    execute_from_command_line(argv=argv)


if __name__ == '__main__':
    main()
    logger.info("Generating coverage HTML report")
    cov.save()
    cov.html_report()
    logger.info("All done")
