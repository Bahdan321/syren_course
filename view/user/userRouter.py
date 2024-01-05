from view.user.schemas import Create_user
from view.user import crud

from fastapi import APIRouter

user_router = APIRouter(prefix="/users", tags=["user"])

@user_router.post("/")
async def create_user(user: Create_user ):
    return crud.create_user(user_in=user)