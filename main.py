from db.base import Base
from db.models.db_helper import DatabaseHeler, db_helper
import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI

from routers import main_api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield



app = FastAPI(
    title="Syren Course"
)

app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

