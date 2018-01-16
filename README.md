[![Build Status](https://img.shields.io/travis/ixc/django-model-settings.svg)](https://travis-ci.org/ixc/django-model-settings)
[![Coverage Status](https://img.shields.io/coveralls/ixc/django-model-settings.svg)](https://coveralls.io/github/ixc/django-model-settings)
[![Version](https://img.shields.io/pypi/v/django-model-settings.svg)](https://pypi.python.org/pypi/django-model-settings)

# Overview

Provides persistant settings that can be edited in the Django admin. Settings
can be any data type via polymorphic models. You can add support for new or
custom types of settings.

Includes template tags and a dict-like interface to access settings, with an
option to automatically create non-existent settings on first access with a
default value.

# How to Use in Templates

Load the tag library:
```html+django
{% load model_settings_tags %}
```
Get a settings object that will fetch and cache all setting values on first
access:
```html+django
{% get_settings as settings %}

{# Fetch and cache all the settings, then render `some_setting`. #}
{{ settings.some_setting }}
    
{# Only hits the database if `other_setting` isn't already in the cache. #}
{{ settings.other_setting }}
```
Settings can be used to store snippets of content or configuration:
```html+django
{% if settings.some_boolean_configuration %}
   ... {{ settings.some_text_content }} ...
{% endif %}
```
Get a settings object that will automatically create non-existent settings with
an empty string as the default value:
```html+django
{% get_settings "" as settings %}

{# Create `new_setting`, if it doesn't already exist. #}
{{ settings.new_setting }}
```
If you only need to get one setting, or want to use a different default value
for a particular setting:
```html+django
{% get_setting "some_content" %}

{# Get or create a boolean setting that is enabled by default. #}
{% get_setting "some_feature" True as some_feature %}
{% if some_feature %}...{% endif %}
```
You can also use the included `model_settings.context_processor.settings`
context processor to add `SETTINGS` to all `RequestContext` objects. This
will be a `SettingDict` object that automatically creates non-existent
settings on first access with an empty string as the default value.

# How to use in Views

Get a dict-like object for all settings:
```python
from model_settings.models import Setting
settings = Setting.objects.as_dict()
```
Get a settings object that only populates the cache for a subset of settings:
```python
settings = Setting.objects.filter(name__startswith='foo').as_dict()
```
Get a settings object that will automatically create non-existent settings with
an empty string as the default value:
```python
settings = Setting.object.as_dict(default='')
```
# Creating Settings

You can create settings of a particular type by using the `SettingValueModel`
subclasses:
```python
Boolean.objects.create(name='foo', value=True)
Integer.objects.create(name='bar', value=123)
```
You can automatically create a setting of the correct type by using the
`Setting` model directly:
```python
Setting.objects.create(name='foo', value=True)
Setting.objects.create(name='bar', value=123)
```
Each `SettingValueModel` subclass has a `value_type` attribute and an
`is_compatible()` method, which are used to determine whether or not the
subclass can store a particular value.

# Custom Setting Types

Support for common types of settings is built-in, e.g. boolean, date, datetime,
decimal, file, float, integer, text, and time. You can add support for custom
types by subclassing `Setting` and `SettingValueModel`:
```python
class Foo(Setting, SettingValueModel):
    value = FooField()
    value_type = FooType
```
If you need more than a simple type check against `value_type` to determine
whether or not a value is comatible, you can override the `is_compatible()`
method.

This method takes a value and should return `True` if the value is
compatible, or `False` if it is not. You can use this to create sub-types
that are rendered differently or utilise a different widget on the admin form.
For example, single line and multi-line text:

```python
class SingleLineText(Setting, SettingValueModel):
    value = models.CharField(max_length=255)

    @classmethod
    def is_compatible(self, value):
        if isinstance(value, unicode) and '\n' not in value:
            return True
        return False

class MultiLineText(Setting, SettingValueModel):
    value = models.TextField()

    @classmethod
    def is_compatible(self, value):
        if isintance(value, unicode) and '\n' in value:
            return True
        return False
```

The `value_type` attribute and `is_compatible()` method are only by
`Setting.objects.create()`, when it tries to determine which subclass to use.

# To Do

  * Customise label, help text, etc. for settings in the admin edit form.
  * Add plugins for Rich Text and Raw code (HTML, CSS, JS) settings.
  * Add tests.
