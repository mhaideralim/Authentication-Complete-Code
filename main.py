from fastapi import FastAPI
from v1.main import app as v1_app
from v1.routers import authentication_router

app = FastAPI()

app.mount("/v1", v1_app)

app.include_router(authentication_router.router, prefix="/v1")