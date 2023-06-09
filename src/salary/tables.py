from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password_hash = Column(String)


class Salary(Base):
    __tablename__ = 'salaries'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    salary = Column(Integer)
    date_next_promotion = Column(Date)

    user = relationship('User', backref='salaries')
