from functools import wraps

current_user = {"role": "admin"}

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.get("role") != role:
                raise PermissionError(f"User does not have the required role: {role}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@require_role("admin")
def admin_dashboard():
    return {"message": "Welcome to the admin dashboard!"}


admin_dashboard()  # This will work since current_user has the "admin" role.