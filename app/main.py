
from fastapi import FastAPI
from routers.users import router as user_routes
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_NAME = os.getenv("MONGODB_NAME")
print("LOGGING --> ", MONGODB_NAME)

app = FastAPI()


def start_app():
    ''' Initialises and configures application 
        including routes and api settings.
    '''
    app.include_router(user_routes)
    print("App initialised!!")


start_app()
