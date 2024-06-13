# tests/test_models.py

import pytest
from app.models import User, Transaction  # Adjust imports as per your project structure
from app import Session, Base, engine

@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_user_model(setup_database):
    session = Session()

    # Test data
    user = User(username='test_user', password='password123', email='test_user@example.com')

    # Add to session and commit
    session.add(user)
    session.commit()

    # Retrieve user from database and assert
    user_db = session.query(User).filter_by(username='test_user').first()
    assert user_db is not None
    assert user_db.username == 'test_user'

    # Clean up
    session.rollback()
    session.close()

def test_transaction_model(setup_database):
    # Implement test for Transaction model similarly
    pass
