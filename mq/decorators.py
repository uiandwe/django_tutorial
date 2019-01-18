import functools


def decorator(view_func):
    @functools.wraps(view_func)
    def new_view_func(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        return response
    return new_view_func