# Flask OpenAI App

## Overview
This project creates a simple Flask server that exposes an endpoint to ask a question. The server sends the question to an OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database. The server and the database are dockerized and run with Docker Compose. A pytest test is also included.

## Setup Instructions

### Prerequisites
- Docker
- Docker Compose

### Steps   
1. Clone the repository.
2. Navigate to the project directory.
3. Create a `.env` file and add your OpenAI API key:

4. Build and run the containers:
# docker-compose up --build
