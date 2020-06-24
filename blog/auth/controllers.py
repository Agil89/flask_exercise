from flask import Flask,Blueprint,render_template,flash,redirect,request,session
from blog.auth.models import create_user,check_user
from blog.auth.forms import RegisterForm,LoginForm
from blog.core.utils import login_required



auth = Blueprint(__name__,'auth')

@auth.route('/register',methods=['GET','POST'])
def register():
    forms = RegisterForm()
    print(forms.data)
    if forms.validate_on_submit():
        create_user(**forms.data)
        flash('Succesfully registered,sign in please.')
        return redirect('/sign')
    context = {
        'forms': forms
    }
    return render_template('auth/register.html',**context)

@auth.route('/sign',methods=['GET','POST'])
def sign_in():
    forms = LoginForm()
    next_page = request.args.get('next','/')
    form_error_message = None
    if request.method == 'POST' and forms.validate_on_submit():
        user = check_user(forms.data['username'],forms.data['password'])
        if user:
            session['user_id'] = user['id']
            session['loginned'] = True
            return redirect(next_page)
        else:
            form_error_message = 'User not found.'
    context = {
        'forms':forms,
        'form_error_message': form_error_message
    }
    return render_template('auth/sign.html',**context)