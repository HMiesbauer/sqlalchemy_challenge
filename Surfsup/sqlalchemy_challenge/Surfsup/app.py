#Import the dependencies
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.automap import automap_base
from datetime import datetime, timedelta

# Create an app, being sure to pass __name__
app = Flask(__name__)

# Define the database URL as a configuration variable (ChatGPT, personal communication, February 27, 2024)
app.config['DATABASE_URL'] = 'sqlite:///hawaii.sqlite'

# Get the database URL from the app configuration (ChatGPT, personal communication, February 27, 2024)
database_url = app.config['DATABASE_URL']

# Create SQLAlchemy engine using the database URL (ChatGPT, personal communication, February 27, 2024)
engine = create_engine(app.config['DATABASE_URL'])

#Use automap_base() and reflect the database schema 
Base = automap_base()
Base.prepare(autoload_with=engine)

#Create session
session = Session(engine)

#Save references to the tables in the sqlite file
measurement = Base.classes.measurement
station = Base.classes.station

#Start at the homepage, list all the available routes
@app.route("/")
def home():
     return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
     )

#Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    return (
        f"Available Route:<br/>"
        f"/api/v1.0/precipitation<br/>"
    )
#Calculate the date one year from the last date in data set. #stackoverflow https://stackoverflow.com/questions/19480028/attributeerror-datetime-module-has-no-attribute-strptime
    last_date = session.query(func.max(measurement.date)).scalar()
    one_year_ago = datetime.datetime.strptime(last_date, '%Y-%m-%d') - datetime.timedelta(days=365)

#Perform a query to retrieve the data and precipitation scores
    precipitation_data = session.query(measurement.date, measurement.prcp).filter(measurement.date >= one_year_ago).all()

#Convert the query results from your precipitation analysis to a dictionary
#Use date as key, prcp as value. (ChatGPT, personal communication, February 27, 2024)
    precipitation_dictonary = {date: prcp for date, prcp in precipitation_data}

    return jsonify(precipitation_dictonary)

#Station route
@app.route("/api/v1.0/station")
def station():
     return (
        f"Available Route:<br/>"
        f"/api/v1.0/station<br/>"
     )

#TOBS route
@app.route("/api/v1.0/tobs/")
def tobs():
     return (
        f"Available Route:<br/>"
        f"/api/v1.0/tobs<br/>"
     )

if __name__ == "__main__":
    app.run(debug=True)


