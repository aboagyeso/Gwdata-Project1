import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///db/rodents_db.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# Save reference to the table
data= Base.classes.rodents_sightings

# Create our session (link) from Python to the DB
session = Session(engine)



app = Flask(__name__)



@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


@app.route("/sightings")
def sightings_data():
    
    # Query for the top 10 emoji data
    sightings= session.query(data.WARD, func.count(data.SERVICECODEDESCRIPTION)).\
        group_by(data.WARD).\
        order_by(data.SERVICECODEDESCRIPTION.desc()).all()

    ward=[]
    count=[]
    for sighting in sightings:
        ward.append(sighting[0])
        count.append(sighting[1])

    # Generate the plot trace
    trace = {
        "x": ward,
        "y": count,
        "type": "bar"
    }
    return jsonify(trace)

@app.route(/"leaf")
def sightings_data():
    

    sightings= session.query(data.WARD, data.LATITUDE, data.LONGITUDE, func.count(data.SERVICECODEDESCRIPTION)).\
        group_by(data.WARD).\
        order_by(data.SERVICECODEDESCRIPTION.desc()).all()

    ward=[]
    longitude=[]
    latitude=[]
    count=[]
    for sighting in sightings:
        ward.append(sighting[0])
        count.append(sighting[3])
        latitude.append(sighting[1])
        longitude.append(sighting[2])

    # Generate the plot trace
    trace = {
        "x": latitude,
        "y": longitude
    }
    return jsonify(trace)

   