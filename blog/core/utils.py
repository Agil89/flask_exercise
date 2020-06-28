# from flask import session,redirect,flash,request
# 
# 
# def login_required(f):
#     def wrapper(*args, **kwargs):
#         if not session.get('loginned'):
#             next_page = request.full_path
#             flash('Please sign in before enter.')
#             return redirect(f'/sign?next={next_page}')
#         return f(*args, **kwargs)
#     wrapper.__name__= f.__name__
#     return wrapper
from blog import UPLOADED_FILES_DIR,os
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import url_for

def save_file(f):
    filename = secure_filename(f.filename)
    filename = f'{datetime.now()}_{filename}'
    file_dir = (os.path.join(
        UPLOADED_FILES_DIR, filename
    ))
    f.save(file_dir)
    file_path = url_for('uploaded_file',filename=filename)
    return file_path