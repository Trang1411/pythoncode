from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://remove:123456@192.168.1.6:5432/mydb1')
# create 1 obj Base
Base = declarative_base()

#define 1 table
class Person(Base):
    __table_args__ = {'schema': 'autotest'}
    __tablename__= 'person'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    address = Column(String)
    position = Column(String)
    department_id = Column(Integer)

class Department(Base):
    __table_args__ = {'schema': 'autotest'}
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

#create 1 session
Session = sessionmaker(bind=engine)
session = Session()

#Function insert data into table
def insert_data(id, user_name, email, address, position, department_id):
    #create object (= constructor)
    new_record = Person(id=id, user_name=user_name, email=email, address=address, position=position, department_id=department_id)
    #add in session
    session.add(new_record)
    #commit -> save data in database
    session.commit()

#Function get data according to condition
def get_person_by_id(id):
    # use filter
    query = session.query(Person).filter(Person.id == id)
    #return list persons
    return query.all()
# def create_person(Person):

