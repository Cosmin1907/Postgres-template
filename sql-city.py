from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "City" table
class City(base):
    __tablename__ = "City"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    population = Column(Integer)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# create an instance of city
amsterdam = City(
    name = "Amsterdam",
    population = 1000000
)

paris = City(
    name = "Paris",
    population = 3000000
)

constanta = City(
    name = "Constanta",
    population = 750000
)

# add each instance of programmers to our session
#session.add(amsterdam)
#session.add(paris)
#session.add(constanta)


# commit our session to the database
#session.commit()
cities = session.query(City)
for city in cities: 
    print(city.id, city.name, city.population, sep=" | ")