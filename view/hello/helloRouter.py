from fastapi import APIRouter

hello_router = APIRouter(prefix="/hello")

@hello_router.get("/")
async def hello(name: str):
    name = name.strip().title()
    return {"message": f"Hello {name}"}

@hello_router.get("/index/")
async def index():
    return {"message": "Hello Index!"}
