"""
Template tags that work with the provided concrete ``Setting`` model. If you
have created your own ``SettingModel`` subclass, you can subclass these tags
and override the ``setting_model`` attribute to make them work with your model.
"""

from classytags.arguments import Argument
from classytags.core import Options, Tag
from classytags.helpers import AsTag
from django import template
from model_settings.models import Setting

register = template.Library()

class GetSettings(AsTag):
    """
    Adds a ``SettingDict`` object to the context.

        {% get_settings [default] [as <varname>] %}

    If a setting doesn't exist on access and ``default`` has been provided, a
    setting will be created with ``default`` as its value.
    """

    name = 'get_settings'
    options = Options(
        Argument('default', default=None, required=False),
        'as',
        Argument('varname', resolve=False),
    )
    setting_model = Setting

    def get_value(self, context, default):
        """
        Returns a ``SettingDict`` object.
        """
        if default is None:
            settings = self.setting_model.objects.as_dict()
        else:
            settings = self.setting_model.objects.as_dict(default=default)
        return settings

register.tag(GetSettings)

class GetSetting(AsTag):
    """
    Returns the value of the named setting, or adds it to the context.

        {% get_setting <name> [default] [as <varname>] %}

    If the setting doesn't exist and ``default`` has been provided, a setting
    will be created with ``default`` as its value.

    Use this instead of ``{% get_settings %}`` if you only need to get a single
    setting, or in addition if you want to define a different default for a
    single setting.
    """

    name = 'get_setting'
    options = Options(
        Argument('name'),
        Argument('default', default=None, required=False),
        'as',
        Argument('varname', resolve=False, required=False),
    )
    setting_model = Setting

    def get_value(self, context, name, default):
        """
        Returns the value of the named setting.
        """
        settings = self.setting_model.objects.filter(name=name)
        if default is None:
            settings = settings.as_dict()
        else:
            settings = settings.as_dict(default=default)
        value = settings[name]
        return value

register.tag(GetSetting)

class BlockSetting(Tag):
    """
    A block tag version of ``{% get_setting %}``. The default value is provided
    by the block content instead of a tag argument.

        {% block_setting <name> %}
            <default>
        {% end_block_setting %}

    Use this instead of ``{% get_setting %}`` when the default value can't be
    passed as a tag argument, e.g. multiple lines of text or template tags.
    """

    name = 'block_setting'
    options = Options(
        Argument('name'),
        blocks=[('end_block_setting', 'nodelist')],
    )
    setting_model = Setting

    def render_tag(self, context, name, nodelist):
        """
        Returns the value of the named setting.
        """
        # Use `try` and `except` instead of `setdefault()` so we can skip
        # rendering the nodelist when the setting already exists.
        settings = self.setting_model.objects.filter(name=name).as_dict()
        try:
            value = settings[name]
        except KeyError:
            value = settings[name] = nodelist.render(context)
        return value

register.tag(BlockSetting)
