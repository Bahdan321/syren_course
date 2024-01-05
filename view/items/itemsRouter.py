from typing import Annotated

from fastapi import APIRouter, Path

items_router = APIRouter(prefix="/items")


@items_router.get("/")
async def get_items():
    return [
        "Item1",
        "Item2",
        "Item3",
        "Item4",
        "Item5",
    ]

@items_router.get("/{item_id}/")
async def get_items_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id,
        }
    }
    