from datetime import datetime

from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_stormpath import (
    user,
    login_required,
    login_user,
    logout_user,
    User,
    StormpathError,
    StormpathManager,
)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '2pSfwmbRhv1QEH04/RthcE4nU16F13OX9YVTGLqr+b8'
app.config['STORMPATH_API_KEY_FILE'] = 'apiKey.properties'
app.config['STORMPATH_APPLICATION'] = 'myBlogProject'

stormpath_manager = StormpathManager(app)

if __name__ == '__main__':
    app.run()
