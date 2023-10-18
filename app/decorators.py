from rest_framework import status
from django.http import HttpResponse


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse({"error: Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    return wrapper_func
