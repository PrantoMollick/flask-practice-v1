from flask import render_template, Blueprint


core = Blueprint('core', __name__)


@core.route('/about')
def about():
    return render_template('about.html'), 200

@core.route('/contact')
def contact():
    return render_template('contact.html'), 200