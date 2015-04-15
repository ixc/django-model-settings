try:
    from django.db import migrations  # noqa
except ImportError:
    from django.core.exceptions import ImproperlyConfigured
    message = """
These migrations are for use with Django 1.7 and above. For Django 1.6 and
below, upgrade to South 1.0 or add the following to your settings:

    SOUTH_MIGRATION_MODULES = {
        'model_settings': 'model_settings.south_migrations',
    }
"""
    raise ImproperlyConfigured(message)
