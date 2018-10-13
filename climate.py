#%matplotlib notebook
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct
import datetime as dt
import numpy as np
from flask import Flask

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)

@app.route('/')
def home():
   return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"

    )
@app.route('/api/v1.0/precipitation')  
def precipitation():
    last_year = timedelta(days=365)
    one_year_tobs=session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > (datetime.datetime.today()-last_year)).all()
    plist = []
    for row in one_year_tobs:
        plist.append({"station": row[0], "date": row[1], "prcp": row[2]})

    return jsonify(plist)


@app.route('/api/v1.0/stations')
def stations():
    stations = session.query(Station.station, Station.name).all()
    station_list = []
    for row in stations:
        stationList.append({"station": row[0], "name": row[1]})

    return jsonify(stationList)

@app.route('/api/v1.0/tobs')
def tobs(): 
    year = timedelta(days=365)
    one_year_tobs = session.query(Measurement.date, Measurement.tobs, Measurement.station).filter(Measurement.date > (datetime.datetime.today()-year)).all()
    tobsList = []
    for row in tobs:
        tobsList.append({"station": row[0], "date": row[1], "tob": row[2]})

    return jsonify(tobsList)


@app.route('/api/v1.0/<start>')
def startDate(start):
 start_data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), \
 func.avg(Measurement.tobs).filter(Measurement.date >= start).all()
  temp_dict = {'TMIN':temp_data[0][0], 'TMAX':temp_data[0][1], 'TAVG':temp_data[0][2]}
    if temp_dict['TMIN'] != None:
        return jsonify(temp_dict)

    return jsonify({"error": f"{start} data not found."}), 404

@app.route('/api/v1.0/<start>/<end>')
def rangeData(start, end):
    temp_data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), \
    func.avg(Measurement.tobs).filter(Measurement.date >= start)\
    .filter(Measurement.date <= end).all()
    temp_dict = {'TMIN':temp_data[0][0], 'TMAX':temp_data[0][1], 'TAVG':temp_data[0][2]}
    if temp_dict['TMIN'] != None:
        return jsonify(temp_dict)

    return jsonify({"error": f"Data between {start} and {end} not found."}), 404    

if __name__ == '__main__':
    app.run(debug=True)