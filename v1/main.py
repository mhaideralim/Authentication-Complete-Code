from fastapi import FastAPI

from v1.routers import authentication_router

app = FastAPI()

app.include_router(authentication_router.router)