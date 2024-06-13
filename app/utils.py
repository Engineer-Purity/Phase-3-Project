# app/utils.py

from datetime import date
from app.models import Base, User, Transaction
from app import engine, Session

def init_db():
    Base.metadata.create_all(engine)
    session = Session()

    # Example data for testing
    user1 = User(username='alice', password='password123', email='alice@example.com')
    user2 = User(username='bob', password='password456', email='bob@example.com')

    transaction1 = Transaction(user_id=1, amount=100.0, date=date.today(), description='Groceries')
    transaction2 = Transaction(user_id=2, amount=50.0, date=date.today(), description='Fuel')

    session.add_all([user1, user2, transaction1, transaction2])
    session.commit()

def add_user(username, password, email):
    session = Session()
    user = User(username=username, password=password, email=email)
    session.add(user)
    session.commit()
    return user

def add_transaction(user_id, amount, date, description):
    session = Session()
    transaction = Transaction(user_id=user_id, amount=amount, date=date, description=description)
    session.add(transaction)
    session.commit()
    return transaction

def get_transactions():
    session = Session()
    return session.query(Transaction).all()
