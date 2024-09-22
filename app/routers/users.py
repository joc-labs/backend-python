
from fastapi import APIRouter, HTTPException
from schemas.users import *
from schemas.responses import GenericResponse
from config.mongo import mongodb
from constants.collections import *

router = APIRouter()


@router.post("/user/create", response_model=GenericResponse)
async def create_user(user_creation: UserCreate):
    try:
        user_collection = mongodb.get_collection(USER_COLLECTION)
        user_object = User(
            name=user_creation.name,
            email=user_creation.email,
            password_hash=user_creation.password_hash,
            is_active=True
        )

        # Insert object
        result = await user_collection.insert_one(user_object.model_dump())
        if result:
            return GenericResponse(message="User registered successfully!")
        else:
            raise HTTPException(status_code=400, detail="User creation failed")
    except Exception as error:
        print("Error on user/create: ", error)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/user/info", response_model=User)
async def get_user_info():
    try:
        user_mock = User(name="hello", email="hello@gmail.com",
                         password_hash="hashthere", is_active=True)
        return user_mock
    except Exception as error:
        print("Error on user/info: ", error)
        raise HTTPException(status_code=500, detail="Internal server error")
