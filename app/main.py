from fastapi import FastAPI
from controller.routes import router
from service.utils import ensure_directory_exists

app = FastAPI()

ensure_directory_exists('assets/doc/plot')

app.include_router(router)