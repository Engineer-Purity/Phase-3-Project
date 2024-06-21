# app/models.py

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String(200))

    user = relationship("User", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(user_id={self.user_id}, amount={self.amount}, date={self.date}, description='{self.description}')>"
