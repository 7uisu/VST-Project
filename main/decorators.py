from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth import REDIRECT_FIELD_NAME

def login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                print(f'Redirecting to {login_url}')  # Debug print statement
                return redirect(f'/{login_url}?{redirect_field_name}={request.get_full_path()}')
            return view_func(request, *args, **kwargs)
        return _wrapped_view

    if function:
        return decorator(function)
    return decorator

def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='admin-login'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated or not request.user.is_admin_user:
                print(f'Redirecting to {login_url}')  # Debug print statement
                return redirect(f'/{login_url}?{redirect_field_name}={request.get_full_path()}')
            return view_func(request, *args, **kwargs)
        return _wrapped_view

    if function:
        return decorator(function)
    return decorator
