from starlette.config import Config


config = Config(".env")

DEBUG = config('DEBUG', cast=bool, default=True)
VERSION = config("VERSION", default="0.1.0")
ENV = config("ENVIRONMENT", default="local")

SHOW_DOCS = ENV in ("local", "staging")