"""
Settings for REST framework are all namespaced in the rest_framework setting.
For example your project's `settings.py` file might look like this:

rest_framework = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer',
    )
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.TemplateHTMLRenderer',
    )
}

This module provides the `api_setting` object, that is used to access
REST framework settings, checking for user settings first, then falling
back to the defaults.
"""
from __future__ import unicode_literals
from django.test.signals import setting_changed
from django.conf import settings
from django.utils import six
from restful import ISO_8601  #iso_8601 is utf-8
UTF_8 = ISO_8601
from restful.compat import importlib

USER_SETTINGS = getattr(settings, 'restful', None)

DEFAULTS = {
    # Base API policies
    'DEFAULT_RENDERER_CLASSES': (
        'restful.renderers.JSONRenderer',
        'restful.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'restful.parsers.JSONParser',
        'restful.parsers.FormParser',
        'restful.parsers.MultiPartParser'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'restful.authentication.SessionAuthentication',
        'restful.authentication.BasicAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'restful.permissions.AllowAny',
    ),
    'DEFAULT_THROTTLE_CLASSES': (),
    'DEFAULT_CONTENT_NEGOTIATION_CLASS': 'restful.negotiation.DefaultContentNegotiation',
    'DEFAULT_METADATA_CLASS': 'restful.metadata.SimpleMetadata',
    'DEFAULT_VERSIONING_CLASS': None,

    # Generic view behavior
    'DEFAULT_PAGINATION_CLASS': 'restful.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': (),

    # Throttling
    'DEFAULT_THROTTLE_RATES': {
        'user': None,
        'anon': None,
    },
    'NUM_PROXIES': None,

    # Pagination
    'PAGE_SIZE': None,

    # Filtering
    'SEARCH_PARAM': 'search',
    'ORDERING_PARAM': 'ordering',

    # Versioning
    'DEFAULT_VERSION': None,
    'ALLOWED_VERSIONS': None,
    'VERSION_PARAM': 'version',

    # Authentication
    'UNAUTHENTICATED_USER': 'django.contrib.auth.models.AnonymousUser',
    'UNAUTHENTICATED_TOKEN': None,

    # View configuration
    'VIEW_NAME_FUNCTION': 'restful.views.get_view_name',
    'VIEW_DESCRIPTION_FUNCTION': 'restful.views.get_view_description',

    # Exception handling
    'EXCEPTION_HANDLER': 'restful.views.exception_handler',
    'NON_FIELD_ERRORS_KEY': 'non_field_errors',

    # Testing
    'TEST_REQUEST_RENDERER_CLASSES': (
        'restful.renderers.MultiPartRenderer',
        'restful.renderers.JSONRenderer'
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'multipart',

    # Browser enhancements
    'FORM_METHOD_OVERRIDE': '_method',
    'FORM_CONTENT_OVERRIDE': '_content',
    'FORM_CONTENTTYPE_OVERRIDE': '_content_type',
    'URL_ACCEPT_OVERRIDE': 'accept',
    'URL_FORMAT_OVERRIDE': 'format',

    'FORMAT_SUFFIX_KWARG': 'format',
    'URL_FIELD_NAME': 'url',

    # Input and output formats
    'DATE_FORMAT': UTF_8,
    'DATE_INPUT_FORMATS': (UTF_8,),

    'DATETIME_FORMAT': UTF_8,
    'DATETIME_INPUT_FORMATS': (UTF_8,),

    'TIME_FORMAT': UTF_8,
    'TIME_INPUT_FORMATS': (UTF_8,),

    # Encoding
    'UNICODE_JSON': True,
    'COMPACT_JSON': True,
    'COERCE_DECIMAL_TO_STRING': True,
    'UPLOADED_FILES_USE_URL': True,

    # Pending deprecation:
    'PAGINATE_BY': None,
    'PAGINATE_BY_PARAM': None,
    'MAX_PAGINATE_BY': None
}


# List of settings that may be in string import notation.
IMPORT_STRINGS = (
    'DEFAULT_RENDERER_CLASSES',
    'DEFAULT_PARSER_CLASSES',
    'DEFAULT_AUTHENTICATION_CLASSES',
    'DEFAULT_PERMISSION_CLASSES',
    'DEFAULT_THROTTLE_CLASSES',
    'DEFAULT_CONTENT_NEGOTIATION_CLASS',
    'DEFAULT_METADATA_CLASS',
    'DEFAULT_VERSIONING_CLASS',
    'DEFAULT_PAGINATION_CLASS',
    'DEFAULT_FILTER_BACKENDS',
    'EXCEPTION_HANDLER',
    'TEST_REQUEST_RENDERER_CLASSES',
    'UNAUTHENTICATED_USER',
    'UNAUTHENTICATED_TOKEN',
    'VIEW_NAME_FUNCTION',
    'VIEW_DESCRIPTION_FUNCTION'
)


def perform_import(val, setting_name):
    """
    If the given setting is a string import notation,
    then perform the necessary import or imports.
    """
    if val is None:
        return None
    elif isinstance(val, six.string_types):
        return import_from_string(val, setting_name)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item, setting_name) for item in val]
    return val


def import_from_string(val, setting_name):
    """
    Attempt to import a class from a string representation.
    """
    try:
        # Nod to tastypie's use of importlib.
        parts = val.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except ImportError as e:
        msg = "Could not import '%s' for API setting '%s'. %s: %s." % (val, setting_name, e.__class__.__name__, e)
        raise ImportError(msg)


class APISettings(object):
    """
    A settings object, that allows API settings to be accessed as properties.
    For example:

        from rest_framework.settings import api_settings
        print(api_settings.DEFAULT_RENDERER_CLASSES)

    Any setting with string import paths will be automatically resolved
    and return the class, rather than the string literal.
    """
    def __init__(self, user_settings=None, defaults=None, import_strings=None):
        self.user_settings = user_settings or {}
        self.defaults = defaults or DEFAULTS
        self.import_strings = import_strings or IMPORT_STRINGS

    def __getattr__(self, attr):
        if attr not in self.defaults.keys():
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Coerce import strings into classes
        if val and attr in self.import_strings:
            val = perform_import(val, attr)

        # Cache the result
        setattr(self, attr, val)
        return val


api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)


def reload_api_settings(*args, **kwargs):
    global api_settings
    setting, value = kwargs['setting'], kwargs['value']
    if setting == 'restful':
        api_settings = APISettings(value, DEFAULTS, IMPORT_STRINGS)


setting_changed.connect(reload_api_settings)
