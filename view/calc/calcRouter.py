from fastapi import APIRouter

calc_router = APIRouter(prefix="/calc")

@calc_router.get("/add/")
async def add(a:int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a+b,
    }
