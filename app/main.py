from fastapi import FastAPI
from controller.routes import router

app = FastAPI()

app.include_router(router)