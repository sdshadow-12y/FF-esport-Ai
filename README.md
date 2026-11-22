# Python API

## Run locally
1. Install Python 3.11+.
2. `cd backend`
3. Create a virtual environment: `python -m venv .venv` and activate it.
4. Install: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and add your OpenAI API key.
6. Start: `uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`
7. Open `http://127.0.0.1:8000/docs`.

All five AI endpoints are implemented. Without an API key they return an explicit setup response, not fabricated AI output. Firebase Admin SDK is included as an optional dependency; add a private service account path only after configuring Firebase. Authentication enforcement and persistent Firestore writes are not enabled in this starter package yet.
