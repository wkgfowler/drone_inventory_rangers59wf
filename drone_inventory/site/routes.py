from flask import Blueprint, render_template
from flask_login import login_required

site = Blueprint('site', __name__, template_folder='site_templates')

"""
Blueprint Configuration
The first argument, "site" is the Blueprint's name, which is used by Flask's routing system.

The second argument, __name__, is the Blueprint's import name, which Flask uses to locate the Blueprint resources.

The last argument, 'template_folder', is the Blueprint's HTML template folder, which tells the Blueprint which HTML files to use for specific routes.
"""
@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

