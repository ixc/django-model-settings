import django
from django.db import transaction


def get_all_related_objects(opts):
    if django.VERSION < (1, 8):
        return opts.get_all_related_objects()
    else:
        return [r for r in opts.related_objects if not r.field.many_to_many]


class SettingDict(dict):
    """
    Provides a read/write dict-like interface for ``Setting`` objects.

    Caches setting values for efficiency. Call the ``refresh()`` method to
    re-fetch all values from the database, if the cache becomes stale.
    """

    def __init__(self, model=None, queryset=None, default=None):
        """
        All setting values for the given model or queryset will be lazily
        loaded into the cache on first access.

        If ``default`` is not ``None``, non-existent settings will be created
        on access.
        """
        if model:
            self.model = model
            self.queryset = model.objects.all()
        elif queryset is not None: # Don't evaluate the queryset as a boolean.
            if model:
                raise ValueError(
                    'Only one of `model` or `queryset` can be provided.')
            self.model = queryset.model
            self.queryset = queryset
        else:
            raise ValueError(
                'At least one of `model` or `queryset` must be provided.')
        self.default = default
        self.empty_cache = True
        super(SettingDict, self).__init__()

    def __delitem__(self, key):
        """
        Deletes a setting from the dict and the database.
        """
        # Populate the cache on first access.
        if self.empty_cache:
            self.refresh()
        deleted = self.model.objects.filter(name=key).delete()
        # Only raise a KeyError when deleting if the setting didn't exist in
        # the databases. It's OK if it didn't exist in the cache, as it might
        # be only a subset.
        try:
            super(SettingDict, self).__delitem__(key)
        except KeyError:
            if not deleted:
                raise

    def __getitem__(self, key):
        """
        Returns the setting value for ``key`` from the cache if possible,
        otherwise from the database. Adds values that are fetched from the
        database to the cache.
        """
        # Populate the cache on first access.
        if self.empty_cache:
            self.refresh()
        # Get the value from the cache.
        try:
            value = super(SettingDict, self).__getitem__(key)
        except KeyError:
            # Get the value from the database.
            try:
                value = self.model.objects.get(name=key).value
            except self.model.DoesNotExist:
                if self.default is None:
                    raise KeyError(key)
                # Create setting with default value.
                value = self.default
                self.model.objects.create(name=key, value=value)
            # Update the cache.
            super(SettingDict, self).__setitem__(key, value)
        return value

    def __setitem__(self, key, value):
        """
        Tries to delete and then creates a setting, in case the value type has
        changed. Otherwise, we would need to get, update (if same type), or
        delete and create (if not same type).
        """
        # Populate the cache on first access.
        if self.empty_cache:
            self.refresh()
        # Delete and create.
        with transaction.atomic():
           self.model.objects.filter(name=key).delete()
           self.model.objects.create(name=key, value=value)
        # Update the cache.
        super(SettingDict, self).__setitem__(key, value)

    def refresh(self):
        """
        Updates the cache with setting values from the database.
        """
        # `values_list('name', 'value')` doesn't work because `value` is not a
        # setting (base class) field, it's a setting value (subclass) field. So
        # we have to get real instances.
        args = [(obj.name, obj.value) for obj in self.queryset.all()]
        super(SettingDict, self).update(args)
        self.empty_cache = False
