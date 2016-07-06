from model_settings.models import Setting

def settings(request):
    """
    Adds a ``SettingDict`` object for the ``Setting`` model to the context as
    ``SETTINGS``. Automatically creates non-existent settings with an empty
    string as the default value.
    """
    settings = Setting.objects.all().as_dict(default='')
    context = {
        'SETTINGS': settings,
    }
    return context
