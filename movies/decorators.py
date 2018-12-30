import functools
from . import utils

def decorator(view_func):
    @functools.wraps(view_func)
    def new_view_func(request, *args, **kwargs):
        request = utils.check_rights(request)
        response = view_func(request, *args, **kwargs)
        return response
    return new_view_func