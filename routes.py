from fastapi import APIRouter
from app.schemas import ChatIn, GunIn, SquadIn, GameplayIn, TrainingIn
from app.ai import ask_ai
router = APIRouter()
WEAPONS = ["Trogon", "SKORP", "MAG-7", "MP5 Chip III", "Charge Buster", "M590", "KORD", "M60", "AWM", "M82B Barrett"]
@router.get("/health")
def health(): return {"status":"ok", "service":"sd-ff-ai-backend"}
@router.get("/weapons")
def weapons(): return {"weapons": WEAPONS, "image_policy":"Use only verified matching Free Fire assets; otherwise show a placeholder."}
@router.post("/ai/chat")
def chat(x: ChatIn): return ask_ai("You are an expert Free Fire esports coach. Answer gameplay, weapons, squad and training questions.", x.message)
@router.post("/ai/gun-recommendation")
def guns(x: GunIn): return ask_ai("Recommend only weapons from this verified project list: " + ", ".join(WEAPONS), x.model_dump())
@router.post("/ai/squad-advisor")
def squad(x: SquadIn): return ask_ai("Advise a Free Fire squad of up to four players. Do not invent player stats.", x.model_dump())
@router.post("/ai/gameplay-analysis")
def gameplay(x: GameplayIn): return ask_ai("Analyze only the supplied match statistics and observations. Explicitly mark unknown metrics as unknown.", x.model_dump())
@router.post("/ai/training-coach")
def training(x: TrainingIn): return ask_ai("Create a safe, practical Free Fire training plan with drills and durations.", x.model_dump())
