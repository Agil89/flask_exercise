from flask import Flask,Blueprint,render_template,flash,redirect,request,session
# from blog.auth.models import create_user,check_user
from blog.auth.forms import RegisterForm,LoginForm
# from blog.core.utils import login_required
from flask_login import login_user
from blog.auth.models import User
from blog import db


auth = Blueprint(__name__,'auth')

@auth.route('/register',methods=['GET','POST'])
def register():
    forms = RegisterForm()
    if forms.validate_on_submit():
        user = User(username=forms.username.data,email=forms.email.data,first_name = forms.first_name.data,
                    last_name=forms.last_name.data,password=forms.password.data)
        db.session.add(user)
        db.session.commit()
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
    if request.method == 'POST' and forms.validate_on_submit():
        user = User.query.filter_by(username=forms.username.data).first()
        if user and user.check_password(forms.password.data):
            login_user(user)
            flash('Logged in succesfully.')
            return redirect(next_page)
        else:
            flash('User not found.')
    context = {
        'forms':forms,

    }
    return render_template('auth/sign.html',**context)