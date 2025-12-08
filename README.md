# Project README

This project contains a frontend (React) and a backend (FastAPI). Both
parts run separately and communicate through API calls.

## Requirements

-   Node.js
-   Python 3.10+
-   PostgreSQL

## Backend Setup

1.  Go to the backend folder:

        cd backend

2.  Create a virtual environment and activate it.

3.  Install dependencies:

        pip install -r requirements.txt

4.  Create a `.env` file based on `.env.example`.

5.  Run the server:

        uvicorn app.main:app --reload

Backend runs at:

    http://127.0.0.1:8000

## Frontend Setup

1.  Go to the frontend folder:

        cd frontend

2.  Install dependencies:

        npm install

3.  Start frontend:

        npm start

Frontend runs at:

    http://localhost:3000

## Running Both

Run backend and frontend in two separate terminals.


