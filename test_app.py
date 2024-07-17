import pytest
from app import app, db, QuestionAnswer

# test db
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
# test question - answer
def test_ask_question(client):
    response = client.post('/ask', json={'question': 'What is the day today?'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'question' in data
    assert 'answer' in data
