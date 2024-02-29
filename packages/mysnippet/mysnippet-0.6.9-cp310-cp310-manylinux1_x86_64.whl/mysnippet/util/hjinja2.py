
import json
import string
import uuid


from secrets import choice
from jinja2.ext import Extension
from slugify import slugify as pyslugify
from jinja2 import Environment, StrictUndefined



# jinja2
def jinja2_simple_filter(filter_function):
    class SimpleFilterExtension(Extension):
        def __init__(self, environment):
            super().__init__(environment)
            environment.filters[filter_function.__name__] = filter_function
    SimpleFilterExtension.__name__ = filter_function.__name__
    return SimpleFilterExtension


class JsonifyExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        def jsonify(obj):
            return json.dumps(obj, sort_keys=True, indent=4)
        environment.filters['jsonify'] = jsonify


class RandomStringExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        def random_ascii_string(length, punctuation=False):
            if punctuation:
                corpus = "".join((string.ascii_letters, string.punctuation))
            else:
                corpus = string.ascii_letters
            return "".join(choice(corpus) for _ in range(length))
        environment.globals.update(random_ascii_string=random_ascii_string)


class SlugifyExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        def slugify(value, **kwargs):
            return pyslugify(value, **kwargs)
        environment.filters['slugify'] = slugify


class UUIDExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        def uuid4():
            return str(uuid.uuid4())
        environment.globals.update(uuid4=uuid4)


class ExtensionLoaderMixin:
    def __init__(self, **kwargs):
        context = kwargs.pop('context', {})
        default_extensions = [
            'mysnippet.util.hjinja2.JsonifyExtension',
            'jinja2_time.TimeExtension',
        ]
        extensions = default_extensions + self._read_extensions(context)
        try:
            super().__init__(extensions=extensions, **kwargs)
        except ImportError as err:
            raise Exception(f'Unable to load extension: {err}') from err

    def _read_extensions(self, context):
        try:
            extensions = context['mysnippet']['_extensions']
        except KeyError:
            return []
        else:
            return [str(ext) for ext in extensions]


class StrictEnvironment(ExtensionLoaderMixin, Environment):
    def __init__(self, **kwargs):
        super().__init__(undefined=StrictUndefined, **kwargs)



