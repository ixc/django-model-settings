"""
Provides abstract polymorphic ``Setting`` models that can be used to store
arbitrary settings of different types.
"""

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.fields.files import FieldFile, ImageFieldFile
from django.db.models.query import QuerySet
from model_settings.utils import SettingDict, get_all_related_objects
from polymorphic.manager import PolymorphicManager
try:
    # for django-polymorphic >= 0.8
    from polymorphic.models import PolymorphicModel
except:
    # for django-polymorphic < 0.8
    from polymorphic import PolymorphicModel
from polymorphic.query import PolymorphicQuerySet
import datetime, decimal, posixpath, re, six

### QUERYSETS #################################################################

class SettingQuerySet(PolymorphicQuerySet):

    def as_dict(self, default=None):
        """
        Returns a ``SettingDict`` object for this queryset.
        """
        settings = SettingDict(queryset=self, default=default)
        return settings

    def create(self, name, value):
        """
        Creates and returns an object of the appropriate type for ``value``.
        """
        if value is None:
            raise ValueError('Setting value cannot be `None`.')
        model = Setting.get_model_for_value(value)
        # Call `create()` method on the super class to avoid recursion.
        obj = super(SettingQuerySet, model.objects.all()) \
            .create(name=name, value=value)
        return obj

### MANAGERS ##################################################################

class SettingManager(PolymorphicManager):
    """
    Replaces the default queryset with ``SettingQuerySet``.
    """
    queryset_class = SettingQuerySet

### ABSTRACT MODELS ###########################################################

class SettingModel(PolymorphicModel):
    """
    An abstract setting model. Each concrete subclass provides a distinct
    collection of settings, with its own set of supported data types.
    """
    name = models.CharField(max_length=255, unique=True)
    objects = SettingManager()

    class Meta:
        abstract = True
        ordering = ['name']

    @classmethod
    def get_model_for_value(cls, value):
        """
        Iterates through setting value subclasses, returning one that is
        compatible with the type of ``value``. Calls ``is_compatible()`` on
        each subclass.
        """
        for related_object in get_all_related_objects(cls._meta):
            model = getattr(related_object, 'related_model', related_object.model)
            if issubclass(model, cls):
                if model.is_compatible(value):
                    return model
        raise ValueError(
            'No compatible `SettingValueModel` subclass for %r' % value)

    def __unicode__(self):
        return self.name

class SettingValueModel(models.Model):
    """
    An abstract setting value model. Create a subclass for each data type that
    you want to support in a collection of settings.

    To use the default ``is_compatible()`` method, each subclass must define a
    ``value_type`` attribute.
    """

    class Meta:
        abstract = True

    @classmethod
    def is_compatible(cls, value):
        """
        Returns ``True`` if this model should be used to store ``value``.

        Checks if ``value`` is an instance of ``value_type``. Override this
        method if you need more advanced behaviour. For example, to distinguish
        between single and multi-line text.
        """
        if not hasattr(cls, 'value_type'):
            raise NotImplementedError(
                'You must define a `value_type` attribute or override the '
                '`is_compatible()` method on `SettingValueModel` subclasses.')
        return isinstance(value, cls.value_type)

### CONCRETE MODELS ###########################################################

class Setting(SettingModel):
    # TODO: Why isn't this inherited from the abstract `SettingModel` class?
    objects = SettingManager()

class Boolean(Setting, SettingValueModel):
    value = models.BooleanField(default=False)
    value_type = bool

class Date(Setting, SettingValueModel):
    value = models.DateField()
    value_type = datetime.date

class DateTime(Setting, SettingValueModel):
    value = models.DateTimeField()
    value_type = datetime.datetime

class Decimal(Setting, SettingValueModel):
    value = models.DecimalField(max_digits=20, decimal_places=10)
    value_type = decimal.Decimal

class File(Setting, SettingValueModel):
    value = models.FileField(upload_to='model-settings/files')
    value_type = FieldFile

class Float(Setting, SettingValueModel):
    value = models.FloatField()
    value_type = float

class Image(Setting, SettingValueModel):
    value = models.ImageField(upload_to='model-settings/images')
    value_type = ImageFieldFile

class Integer(Setting, SettingValueModel):
    value = models.IntegerField()
    value_type = int

class Text(Setting, SettingValueModel):
    value = models.CharField(max_length=255)
    value_type = six.text_type

class Time(Setting, SettingValueModel):
    value = models.TimeField()
    value_type = datetime.time
