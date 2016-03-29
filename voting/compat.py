"""
These are utilities functions to deal with differences between Django versions.
"""

#pylint: disable=invalid-name,unused-import,import-error

try:
    from django.contrib.contenttypes.fields import (
        GenericForeignKey, GenericRelation)
except ImportError: # django < 1.8
    from django.contrib.contenttypes.generic import (
        GenericForeignKey, GenericRelation)


def get_model_class(full_name, settings_meta):
    """
    Returns a model class loaded from *full_name*. *settings_meta* is the name
    of the corresponding settings variable (used for error messages).
    """
    from django.core.exceptions import ImproperlyConfigured

    try:
        app_label, model_name = full_name.split('.')
    except ValueError:
        raise ImproperlyConfigured(
            "%s must be of the form 'app_label.model_name'" % settings_meta)

    model_class = None
    try:
        from django.apps import apps
        model_class = apps.get_model(app_label, model_name)
    except ImportError: # django < 1.7
        from django.db.models import get_model
        model_class = get_model(app_label, model_name)

    if model_class is None:
        raise ImproperlyConfigured(
            "%s refers to model '%s' that has not been installed"
            % (settings_meta, full_name))
    return model_class
