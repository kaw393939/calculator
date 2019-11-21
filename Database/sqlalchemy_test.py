import os
import sys
# from CsvReader.CsvReader import CsvReader
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pprint import pprint
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Subtraction(Base):
    __tablename__ = 'subtraction'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    value1 = Column(Integer, nullable=False)
    value2 = Column(Integer, nullable=False)
    value3 = Column(Integer, nullable=False)


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", backref="addresses")


class Orders(Base):
    __tablename__ = 'orders'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:////web/Sqlite-Data/example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Insert a Person in the person table
new_person1 = Person(name='Keith')
session.add(new_person1)

new_person2 = Person(name='Joe')
session.add(new_person1)

new_person3 = Person(name='Steve')
session.add(new_person1)
session.commit()

# Insert an Address in the address table
new_address1 = Address(post_code='00000', person=new_person1)
session.add(new_address1)

new_address2 = Address(post_code='00000', person=new_person2)
session.add(new_address2)

new_address3 = Address(post_code='00000', person=new_person3)
session.add(new_address3)

new_order = Orders(person=new_person1)
session.add(new_order)
session.commit()
all_people = session.query(Person).join(Address).all()


for person in all_people:
    pprint(person.name)
    for address in person.addresses:
        pprint(address.post_code)

    #print(f'{row.name} lives at {row.post_code}')



objects = [
    Person(name="u1"),
    Person(name="u2"),
    Person(name="u3")
]

#data_objects = CsvReader("Tests/Data/subtraction.csv").return_data_as_objects(Subtraction)


#pprint(all_people)

session.bulk_save_objects(objects)
session.commit()
