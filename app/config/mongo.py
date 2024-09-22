from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_NAME = os.getenv("MONGODB_NAME")


class MongoDB:
    def __init__(self):
        ''' Initialises the database connection.
        '''
        self.client = AsyncIOMotorClient(MONGODB_URI)
        self.database = self.client[MONGODB_NAME]

    def get_collection(self, collection_name: str):
        ''' Retrieves a given connection from
            the database.
        '''
        return self.database[collection_name]


mongodb = MongoDB()
