from flask import Flask, request, jsonify
import openai
from sqlalchemy.orm import Session
from models import Base, QuestionAnswer
from models.database import engine, SessionLocal

# Initialize the Flask application
app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Create database tables
Base.metadata.create_all(bind=engine)

# Create a new database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define the /ask endpoint
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')

    # Call the OpenAI API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=150
    )

    answer = response.choices[0].text.strip()

    # Save the question and answer to the database
    db = next(get_db())
    qa = QuestionAnswer(question=question, answer=answer)
    db.add(qa)
    db.commit()
    db.refresh(qa)

    return jsonify({'question': question, 'answer': answer})

# Define an endpoint to show the history of requests
@app.route('/history', methods=['GET'])
def history():
    db = next(get_db())
    history = db.query(QuestionAnswer).all()
    return jsonify([{'question': q.question, 'answer': q.answer} for q in history])

if __name__ == '__main__':
    app.run(debug=True)
