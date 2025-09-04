from fastapi import FastAPI
from app.controllers.rss_controller import router as rss_router

app = FastAPI()

app.include_router(rss_router)

@app.get("/")
def root():
    return {"message": "API de RSS funcionando!"}
