"""Utility file to seed database from csv file"""

from sqlalchemy import func
from model import User, Places

from model import connect_to_db, db
from server import app


def load_places():
    """Load places from mff_sfpopo into database."""

    print "Places"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate places
    Places.query.delete()

    # Read mff_sfpopo.csv file and insert data
    for row in open("mff_sfpopo.csv"):
        row = row.rstrip()
        place_id, name, address, year_built, description, features, indoor_outdoor, wifi,seating, restroom, coord, place_photo, hours, neighborhood, wheelchair_accessible, url = row.split("|")

        place = Places(place_id=place_id,name=name,address=address,
                       year_built=year_built,description=description,
                       features=features,indoor_outdoor=indoor_outdoor,
                       wifi=wifi,seating=seating,restroom=restroom,coord=coord,
                       place_photo=place_photo,hours=hours,neighborhood=neighborhood,
                       wheelchair_accessible=wheelchair_accessible,url=url)
        # We need to add to the session or it won't ever be stored
        db.session.add(place)

    # Once we're done, we should commit our work
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_places()
