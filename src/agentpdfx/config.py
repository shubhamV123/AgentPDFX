from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    use_ollama:bool = os.getenv("USE_OLLAMA","true").lower() == "true"
    ollama_url: str = os.getenv("OLLAMA_URL", "http://localhost:11434/v1")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    model_id: str = os.getenv("MODEL_ID", "llama2")
    mistral_api_key:str = os.getenv('MISTRAL_API_KEY','')
    google_api_key:str = os.getenv('GOOGLE_API_KEY','')




settings = Settings()
