Instructions:
Create climate analysis about Honolulu, Hawaii through data exploration using SQLAlchemy ORM queries, Pandas, Matplotlib


Code source:
#Calculate the date one year from the last date in data set. #stackoverflow https://stackoverflow.com/questions/19480028/attributeerror-datetime-module-has-no-attribute-strptime
    last_date = session.query(func.max(measurement.date)).scalar()
    one_year_ago = datetime.datetime.strptime(last_date, '%Y-%m-%d') - datetime.timedelta(days=365)

#Convert the query results from your precipitation analysis to a dictionary
#Use date as key, prcp as value. (ChatGPT, personal communication, February 27, 2024)
    precipitation_dictonary = {date: prcp for date, prcp in precipitation_data}
    
    # Define the database URL as a configuration variable (ChatGPT, personal communication, February 27, 2024)
app.config['DATABASE_URL'] = 'sqlite:///hawaii.sqlite'

#Get the database URL from the app configuration (ChatGPT, personal communication, February 27, 2024)
database_url = app.config['DATABASE_URL')

#Create SQLAlchemy engine using the database URL (ChatGPT, personal communication, February 27, 2024)
engine = create_engine(app.config['DATABASE_URL'])

