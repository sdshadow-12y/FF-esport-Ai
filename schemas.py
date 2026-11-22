from pydantic import BaseModel, Field
class ChatIn(BaseModel):
    message: str = Field(min_length=1, max_length=6000)
class GunIn(BaseModel):
    role: str = "flex"
    range: str = "mid-range"
    play_style: str = "balanced"
    map_name: str = "not specified"
class SquadIn(BaseModel):
    players: list[dict] = Field(min_length=1, max_length=4)
    map_name: str = "not specified"
class GameplayIn(BaseModel):
    match_stats: dict
    observations: str = ""
class TrainingIn(BaseModel):
    role: str = "flex"
    skill_level: str = "beginner"
    weaknesses: list[str] = []
    minutes_per_day: int = Field(default=30, ge=5, le=240)
