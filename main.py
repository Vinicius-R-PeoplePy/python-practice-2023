from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender =  Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn 
        self.firstname = first 
        self.lastname = last 
        self.gender = gender 
        self.age = age 

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} {self.gender}, {self.age})"
    

class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid 
        self.description = description
        self.owner = owner 

    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"




engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

p1 = Person(12312, "Mike", "Smith", "m", 35)
p2 = Person(23453, "Bob", "Blue", "m", 40)
p3 = Person(23433, "Angela", "Cold", "f", 22)
session.add(p1)
session.add(p2)
session.add(p3)
session.commit()

t1 = Thing(1, "Car", p1.ssn)
t2 = Thing(2, "Laptop", p1.ssn)
t3 = Thing(3, "PS5", p2.ssn)
t4 = Thing(4, "Tool", p3.ssn)
t5 = Thing(5, "Book", p3.ssn)

session.add(t1)
session.commit()

#results = session.query(Person).all() # select everything from people
#results = session.query(Person).filter(Person.lastname == "Blue")
#results = session.query(Person).filter(Person.age > 25)
#results = session.query(Person).filter(Person.firstname.like("%An%")) # Angela, Anna
#results = session.query(Person).filter(Person.firstname.in_(["Anna", "Mike"]))
results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.firstname == "Anna").all()

for r in results:
    print(r)

