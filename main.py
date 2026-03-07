from contextlib import asynccontextmanager
from fastapi import FastAPI

from items_views import router as items_router
from users.views import router as users_router
from api_v1 import router as products_router
from core.models import Base, db_helper
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(items_router)
app.include_router(users_router)
app.include_router(products_router, prefix=settings.api_v1_prefix)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"Hello": name}
