from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from .model import User
from . import db

authlog = Blueprint('authlog', __name__)

@authlog.route('/login')
def login_page():
    return render_template('login.html')

@authlog.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, password):
        flash('Неправильно набран e-mail или пароль')
        return redirect(url_for('authlog.login_page')) # if the user doesn't exist or password is wrong, reload the page 
   
    login_user(user, remember=remember)
    return redirect(url_for('mainlog.profile'))


@authlog.route('/logout')
def logout_page():
    return render_template('logout.html')

@authlog.route('/register')
def register_page():
    return render_template('register.html')

@authlog.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Такой почтовый ящик уже существует')
        return redirect(url_for('authlog.register_page'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    # code to validate and add user to database goes here
    return redirect(url_for('authlog.login_page'))
    