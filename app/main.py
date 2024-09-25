from fastapi import FastAPI
from routers.users import router as user_routes

app = FastAPI()


def start_app():
    """Initialises and configures application
    including routes and api settings.
    """
    app.include_router(user_routes)
    print("App initialised!!")


start_app()
