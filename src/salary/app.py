from fastapi import FastAPI

from src.salary import api

app = FastAPI()


app.include_router(api.router)
