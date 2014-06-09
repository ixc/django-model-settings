Overview
========

Provides persistant settings that can be edited in the Django admin. Settings
can be any data type via polymorphic models. You can add support for new or
custom types of settings.

Includes template tags and a dict-like interface to access settings, with an
option to automatically create non-existent settings on first access with a
default value.


How to Use in Templates
=======================

Load the tag library::

    {% load model_settings_tags %}

Get a settings object that will fetch and cache all setting values on first
access::

    {% get_settings as settings %}

    {# Fetch and cache all the settings, then render `some_setting`. #}
    {{ settings.some_setting }}

    {# Only hits the database if `other_setting` isn't already in the cache. #}
    {{ settings.other_setting }}

Settings can be used to store snippets of content or configuration::

    {% if settings.some_boolean_configuration %}
        ... {{ settings.some_text_content }} ...
    {% endif %}

Get a settings object that will automatically create non-existent settings with
an empty string as the default value::

    {% get_settings "" as settings %}

    {# Create `new_setting`, if it doesn't already exist. #}
    {{ settings.new_setting }}

If you only need to get one setting, or want to use a different default value
for a particular setting::

    {% get_setting "some_content" %}

    {# Get or create a boolean setting that is enabled by default. #}
    {% get_setting "some_feature" True as some_feature %}
    {% if some_feature %}...{% endif %}


How to use in Views
===================

Get a dict-like object for all settings::

    from model_settings.models import Setting
    settings = Setting.objects.as_dict()

Get a settings object that only populates the cache for a subset of settings::

    settings = Setting.objects.filter(name__startswith='foo').as_dict()

Get a settings object that will automatically create non-existent settings with
an empty string as the default value::

    settings = Setting.object.as_dict(default='')


Custom Settings
===============

Support for core types of settings is built-in, e.g. boolean, date, datetime,
decimal, file, float, integer, text, time. You can add support for custom types
by subclassing ``Setting`` and ``SettingValueModel``::

    class Foo(Setting, SettingValueModel):
        value = FooField()

        def is_compatible(self, value):
            # Return True if `value` is compatible with `FooField`.


TODO
====

*   Customise label, help text, etc. for settings in the admin edit form.
*   Add plugins for Rich Text and Raw code (HTML, CSS, JS) settings.
*   Docs and tests.
