from fastapi import FastAPI

from .rooms import router as rooms_router
from . import config


def get_app() -> FastAPI:
    api_config = {"title": "Planit API"}
    if not config.SHOW_DOCS:
        api_config["openapi_url"] = None
        
    app = FastAPI(**api_config)
    return app


app = get_app()

app.include_router(rooms_router.router)