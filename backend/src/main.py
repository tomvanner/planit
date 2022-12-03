from fastapi import FastAPI

from . import config


def get_app() -> FastAPI:
    api_config = {"title": "Planit API"}
    if not config.SHOW_DOCS:
        api_config["openapi_url"] = None
        
    app = FastAPI(**api_config)
    return app


app = get_app()