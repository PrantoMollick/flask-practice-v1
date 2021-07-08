from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/')
@auth.route('/index')
def index():
    return render_template('index.html'), 200
