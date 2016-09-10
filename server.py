"""Petition Website"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Set a secret key to enable the flask session cookies and the debug toolbar
app.secret_key = 'ABC'

# raises an error if I use an undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

###############################################################################


@app.route('/', methods=['GET'])
def base_homepage():
    """Show homepage"""

    # if the user is logged in, route them to the homepage
    # if 'user_id' in session:
    #     return redirect('/home')
    # if no user if logged in return the base homepage form
    # else:
    return render_template('base_homepage.html')


@app.route('/login', methods=['GET'])
def login_form():
    """Show login form"""

    # if the user is logged in, route them to the homepage
    # if 'user_id' in session:
    #     return redirect('/home')
    # if no user if logged in return the login form
    # else:
    return render_template('login_form.html')


@app.route('/login', methods=['POST'])
def process_login():
    """Process login form"""

    # Get email and password from form
    email = request.form['email']
    password = request.form['password']

    # check if user exists in database
    # user = User.query.filter_by(email=email).first()

    # if user does not exist, redirected them to registration form
    if not user:
        flash('Please create an account')
        return redirect('/register')

    # Check that password matches database, if not flash message and redirect to login form
    elif user.password != password:
        flash('Incorrect password')
        return redirect('/login')

    # if user exists in database and password matches
    else:
        # add the user to the session
        session['user_id'] = user.user_id
        # redirect to the homepage
        return redirect('/home')


@app.route('/logout')
def logout():
    """Log out."""

    # remove the user from the session
    del session['user_id']
    # redirect them to the login page
    return redirect('/')


@app.route('/profile')
def user_profile():
    """Show information about user"""

    # get user id from the session
    # user_id = session['user_id']
    # call function to get user object from session
    # user = user_object()

    return render_template('profile.html')


@app.route('/home')
def home():
    """Homepage"""

    # call function to get user object from session
    # user = user_object()

    return render_template('homepage.html')


@app.route('/register', methods=['GET'])
def registration_form():
    """Show user registration form"""

    return render_template('registration_form.html')


@app.route('/register', methods=['POST'])
def process_registration():
    """Process completed user registration form"""

    # get variables from form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    zipcode = request.form['zipcode']
    email = request.form['email']
    password = request.form['password']

    # check if email exists in database
    # user = User.query.filter_by(email=email).first()

    # if user does not exist, create the account
    if not user:
        # create a new user
        new_user(first_name, last_name, zipcode, email, password)
        # let user know their account was create
        flash('Welcome %s, your account has successfully been created.' % first_name)
        # get user object from database
        user = User.query.filter_by(email=email).first()
        # add user to the session
        session['user_id'] = user.user_id
        # redirect user to the homepage
        return redirect('/home')

    # if email is in database, have the user register with another email
    flash('That email is already taken, please provide another email')
    return redirect('/register')


###############################################################################
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000)
