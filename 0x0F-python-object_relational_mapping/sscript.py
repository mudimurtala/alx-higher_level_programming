"""This script is for practicing SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    email = Column(String(255))

# Updated engine creation line for MySQL
engine = create_engine('mysql+mysqldb://user:ComplexPassword123!@localhost/friday_19th_db', echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(username="funke", email="funke@example.com")
session.add(new_user)
session.commit()
