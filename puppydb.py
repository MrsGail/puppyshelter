import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	#inside Restaurant class
	__tablename__ = 'shelter'

	name = Column(String(80), nullable = False)
	address = Column(String(240))
	city = Column(String(80))
	state = Column(String(20))
	zipCode = Column(String(5))
	website = Column(String(240))
	id = Column(Integer, primary_key = True)

class Puppy(Base):
	#inside MenuItem class
	__tablename__ = 'puppy'

	name = Column(String(80),nullable = False)
	id = Column(Integer, primary_key = True)
	dateOfBirth = Column(Date())
	gender = Column(String(25))
	weight = Column(Numeric(10))
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)


###### insert at end of file #######
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
