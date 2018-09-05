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
m = Base.classes.measurement
s = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)

@app.route('/')
def home():
   return 'home'
@app.route('/api/v1.0/precipitation')  
#Query for the dates and temperature observations from 
# the last year.
#Convert the query results to a Dictionary using
# `date` as the key and `tobs` as the value.
#Return the JSON representation of your dictionary.

def precipitation():
    return print('precip')
@app.route('/api/v1.0/stations')
#Return a JSON list of stations from the dataset.

def stations():
    return print(stations)
@app.route('/api/v1.0/tobs')
#Return a JSON list of Temperature Observations (tobs)
#for the previous year.... return jsonified
def tobs():
    return print(tobs)
@app.route('/api/v1.0/<start>')
#When given the start only, calculate `TMIN`, `TAVG`,
#and `TMAX` for all dates greater than and equal to the 
# start date.... return jsonified
def startDate():
    start_date = 23
    return(start_date)
@app.route('/api/v1.0/<start>/<end>')
#When given the start and the end date, calculate the 
# `TMIN`, `TAVG`, and `TMAX` for dates between the start
# and end date inclusive.
def start_end():
    return(start_date)

if __name__ == '__main__':
    app.run(debug=True)