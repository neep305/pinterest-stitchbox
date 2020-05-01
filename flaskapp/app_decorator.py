from functools import wraps
from flask import session, request, redirect, url_for
from werkzeug.contrib.cache import FileSystemCache


cache = FileSystemCache()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user', None):
            return redirect(url_for('login', next=request.url))
        return f(*args,**kwargs)
    return decorated_function


def cached(timeout=5 * 60, key='view/%s'):
    
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = key % request.path
            rv = cache.get(cache_key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, rv, timeout=timeout)
            return rv
        return decorated_function
    return decorator
