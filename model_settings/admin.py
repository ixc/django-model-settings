from django.contrib import admin
from model_settings.models import Setting, get_all_related_objects
from polymorphic.admin import PolymorphicChildModelAdmin
from polymorphic.admin import PolymorphicParentModelAdmin

### ABSTRACT CLASSES ##########################################################

class SettingModelAdmin(PolymorphicParentModelAdmin):
    """
    An abstract admin class for the ``Setting`` model. Subclasses must define
    ``base_model`` and ``base_admin_class`` attributes.
    """

    list_display = ['__str__', 'get_value']
    polymorphic_list = True

    def get_child_models(self):
        """
        Returns a list of ``(Model, ModelAdmin)`` tuples for ``base_model``
        subclasses.
        """
        child_models = []
        # Loop through all models with FKs back to `base_model`.
        for related_object in get_all_related_objects(self.base_model._meta):
            # Django 1.8 deprecated `get_all_related_objects()`. We're still
            # using it for now with the documented work-around for
            # compatibility with Django <=1.7.
            model = getattr(
                related_object, 'related_model', related_object.model)
            # Only consider `base_model` subclasses.
            if issubclass(model, self.base_model):
                class SettingValueAdmin(self.base_admin_class):
                    pass
                child_models.append((model, SettingValueAdmin))
        return child_models

    def get_value(self, obj):
        """
        Returns the ``value`` field from the child model.
        """
        # Needs `polymorphic_list = True`, otherwise `obj` will be a `Setting`
        # object which has no `value` attribute.
        return obj.value
    get_value.short_description = 'value'

### CONCRETE CLASSES ##########################################################

class SettingValueAdmin(PolymorphicChildModelAdmin):
    base_model = Setting

class SettingAdmin(SettingModelAdmin):
    base_model = Setting
    base_admin_class = SettingValueAdmin

admin.site.register(Setting, SettingAdmin)
