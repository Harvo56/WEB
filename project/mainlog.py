from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
#from . import db

mainlog = Blueprint('mainlog', __name__)

@mainlog.route('/')
def index():
    return render_template('index.html')

@mainlog.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
