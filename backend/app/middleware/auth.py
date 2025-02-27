from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify

def role_required(roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims['identity']['role'] not in roles:
                return jsonify(msg='Forbidden'), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper
