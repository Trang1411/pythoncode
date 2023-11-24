from sqlalchemy import create_engine, Column, Integer, String, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://thutrang:123456@localhost:5432/mydb1')
# create 1 obj Base
Base = declarative_base()

#define 1 table
class Person(Base):
    __table_args__ = {'schema': 'db1'}
    __tablename__= 'Person'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    address = Column(String)
    position = Column(String)
    department_id = Column(Integer)

class Department(Base):
    __table_args__ = {'schema': 'db1'}
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

#create 1 session
Session = sessionmaker(bind=engine)
session = Session()

#Function insert data into table
def insert_person(id, user_name, email, address, position, department_id):
    #create object (= constructor)
    new_record = Person(id=id, user_name=user_name, email=email, address=address, position=position, department_id=department_id)
    #add in session
    session.add(new_record)
    #commit -> save data in database
    session.commit()
    return new_record

#Function get data according to condition
def get_person_by_id(id):
    # use filter
    query = session.query(Person).filter(Person.id == id)
    #return list persons
    return query.first()

#function get all person
def get_all_person():
    query = session.query(Person).filter()
    return query.all()

# function update_person(Person):
def update_user_name_by_id(id):
    data = get_person_by_id(id)
    if (data == None):
        print('id not exists!!!')
    else:
        query = session.query(Person).filter(Person.id == id).update({
            'user_name': 'Ann'
        }, synchronize_session=False)
        person = session.query(Person).filter(Person.id == id)
        session.commit()
        print('after update: ', Person.id, Person.user_name, Person.email)

#functon delete person by id
def delete_person_by_id(id):
    query = session.query(Person).filter(Person.id == id).delete()
    session.commit()
    print("delete success!")
