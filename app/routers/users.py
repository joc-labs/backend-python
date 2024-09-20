
from fastapi import APIRouter, HTTPException
from schemas.users_schemas import User

router = APIRouter()


@router.get("/user/info", response_model=User)
def get_user_info():
    try:
        user_mock = User(name="hello", email="hello@gmail.com",
                         password_hash="hashthere", is_active=True)
        return user_mock
    except Exception as error:
        print("Error on user/info: ", error)
        raise HTTPException(status_code=500, detail="Internal server error")
