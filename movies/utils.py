from django.core.exceptions import PermissionDenied


def check_rights(request):
    
    if request.user.is_anonymous is True:
        return request

    raise PermissionDenied