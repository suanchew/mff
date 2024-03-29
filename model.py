"""Models and database for petition website"""

# from flask import SQLAlchemy

from flask_sqlalchemy import SQLAlchemy

# Connection to the Postgre SQL database through the Flask-SQLAlchemy library
# make a database object
db = SQLAlchemy()


##############################################################################
# Model definitions


class User(db.Model):
    """User of website."""

    # create table named users with appropriate columns
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    profile_photo = db.Column(db.String(500), nullable=True)


class Places(db.Model):
    """Places"""

    # create table named places with appropriate columns
    __tablename__ = 'places'
    place_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    year_built = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    features = db.Column(db.String(100), nullable=True)
    indoor_outdoor = db.Column(db.String(100), nullable=False)
    wifi = db.Column(db.String(100), nullable=True)
    seating = db.Column(db.String(100), nullable=True)
    restroom = db.Column(db.String(100), nullable=True)
    coord = db.Column(db.String(100), nullable=True)
    place_photo = db.Column(db.String(500), nullable=True)
    hours = db.Column(db.String(100), nullable=True)    
    neighborhood = db.Column(db.String(100), nullable=True) 
    wheelchair_accessible = db.Column(db.String(100), nullable=True)
    url = db.Column(db.String(100), nullable=True)

##############################################################################
# Helper functions


def connect_to_db(app, db_uri="postgresql:///mff"):
    """Connect to database in Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == '__main__':
#     # Allows you to work with database directly,
#     # when you run module interactively.

    from server import app
    connect_to_db(app)
    print "Connected to DB"
