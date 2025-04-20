from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from config import config
from models import PredictionModel


client = AsyncIOMotorClient(
    config.MONGODB_URL
)

db = client[config.DB_NAME]

async def init_db():
    await init_beanie(database=db, document_models=[PredictionModel])

try:
    client.server_info()
    print('База данныйга кошулду')
except Exception as e:
    print(f'ошибкаб {e}')