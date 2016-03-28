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
