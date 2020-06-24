from flask import session,redirect,flash,request


def login_required(f):
    def wrapper(*args, **kwargs):
        if not session.get('loginned'):
            next_page = request.full_path
            flash('Please sign in before enter.')
            return redirect(f'/sign?next={next_page}')
        return f(*args, **kwargs)
    wrapper.__name__= f.__name__
    return wrapper