"""Models and database for petition website"""

from flask_sqlalchemy import SQLAlchemy

# Connection to the Postgre SQL database through the Flask-SQLAlchemy library
# make a database object
db = SQLAlchemy()


##############################################################################
# Model definitions


class User(db.Model):
    """User of petition website."""

    # create table named users with appropriate columns
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)


class SavedPetition(db.Model):
    """Petitions that users have saved or signed"""

    # create table named saved_petitions with appropriate columns
    __tablename__ = 'saved_petitions'
    saved_petition_id = db.Column(db.Integer, primary_key=True,
                                  autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    petition_id = db.Column(db.Integer, nullable=False)
    date_signed = db.Column(db.DateTime, nullable=True)
    # define relationship to user
    users = db.relationship('User',
                            backref=db.backref('saved_petitions',
                                               order_by=saved_petition_id))


##############################################################################
# Helper functions


def connect_to_db(app, db_uri="postgresql:///petitions"):
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
