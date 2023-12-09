from contextlib import asynccontextmanager

from fastapi import FastAPI

from planit.database import session_manager
from planit.config import app_config, settings
from planit.users.router import router as user_router


def init_app(use_db=True):
    lifespan = None

    if use_db:
        session_manager.init(settings.DATABASE_URL)

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            yield
            if session_manager._engine is not None:
                await session_manager.close()

    app = FastAPI(**app_config, lifespan=lifespan)
    app.include_router(user_router, prefix="/users", tags=["user"])

    return app


app = init_app()


@app.get("/health")
async def root():
    return {"status": "ok"}