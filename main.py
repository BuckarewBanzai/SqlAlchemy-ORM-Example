from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class PetOwners(Base):
    __tablename__ = "pet_owners"

    owner_id = Column('owner_id', Integer, primary_key=True)
    owner_name = Column('owner_name', String)
    owner_age = Column('owner_age', Integer)


class Pets(Base):
    __tablename__ = "pets"

    pet_id = Column('pet_id', Integer, primary_key=True)
    pet_name = Column('pet_name', String)
    pet_species = Column('pet_species', String)
    pet_age = Column('pet_age', Integer)

#Create our connection to our sqllite Database
engine = create_engine('sqlite:///testdb.db', echo=True)

#Create a database schema based on our pet owner and pet classes above. 
Base.metadata.create_all(bind=engine) 

#Create a session object we can use to communicate with our database
Session = sessionmaker(bind=engine)
session=Session()

#Create our owner and pet objects and pass some data to them
newOwner = PetOwners(owner_name="Mary", owner_age="34")
newPet = Pets(pet_name='Olly', pet_species='Golden Retriever', pet_age='3')

#Add our data objects to our session
session.add(newOwner)
session.add(newPet)

#Commit our data to the database and close our session
session.commit()
session.close()
