
from cachetools import cached
import inspect


@cached(cache={})
def get_class_properties(cls):
    properties = [
        member_name for member_name, member_object in inspect.getmembers(cls)
        if inspect.isdatadescriptor(member_object) and not member_name.startswith('_')
    ]
    return properties