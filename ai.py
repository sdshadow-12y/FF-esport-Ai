from openai import OpenAI
from app.settings import settings

def ask_ai(instructions: str, payload):
    if not settings.openai_api_key:
        return {"configured": False, "message": "AI is not connected yet. Add OPENAI_API_KEY to backend/.env and restart the server.", "demo": True}
    client = OpenAI(api_key=settings.openai_api_key)
    response = client.responses.create(model=settings.openai_model, instructions=instructions + " Return concise, practical advice. Do not invent game statistics or claim live game data.", input=str(payload))
    return {"configured": True, "reply": response.output_text}
