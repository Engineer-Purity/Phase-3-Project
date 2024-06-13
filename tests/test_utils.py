# tests/test_utils.py

import pytest
from app.utils import add_user, add_transaction, get_transactions  # Adjust imports as per your project structure
from app.models import User, Transaction
from app import Session, Base, engine

@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_add_user(setup_database):
    session = Session()

    # Test data
    user = add_user('test_user', 'password123', 'test_user@example.com')

    # Retrieve user from database and assert
    user_db = session.query(User).filter_by(username='test_user').first()
    assert user_db is not None
    assert user_db.username == 'test_user'

    # Clean up
    session.rollback()
    session.close()

def test_add_transaction(setup_database):
    # Implement test for add_transaction similarly
    pass
