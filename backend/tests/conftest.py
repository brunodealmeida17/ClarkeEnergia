import pytest
from main import create_app, db, DEBUG


@pytest.fixture(scope="session")
def test_app():
    
    app = create_app(DEBUG)
    print(DEBUG)
    with app.app_context():
        db.create_all()
    yield app
    

@pytest.fixture
def client(test_app):
    
    with test_app.test_client() as client:
        yield client
