import os
import pytest
from app.models import User  # Adjust imports as per your project structure
from app import Session, Base, engine

# Retrieve the secure password from environment variables
SECURE_PASSWORD = os.getenv("SECURE_PASSWORD", "default_secure_password")


@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_user_model(setup_database):
    session = Session()

    # Test data - Use the secure password constant
    user = User(
        username='test_user',
        password=SECURE_PASSWORD,
        email='test_user@example.com'
    )

    # Add to session and commit
    session.add(user)
    session.commit()

    # Retrieve user from database and assert
    user_db = session.query(User).filter_by(username='test_user').first()
    if user_db is None:
        raise AssertionError("User not found in database")
    if user_db.username != 'test_user':
        raise AssertionError("Username does not match")

    # Clean up
    session.rollback()
    session.close()
