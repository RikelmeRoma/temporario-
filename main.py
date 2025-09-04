from fastapi import FastAPI
from app.routes.rss_router import router as rss_router

app = FastAPI()
app.include_router(rss_router)

@app.get("/")
def root():
    return {"message": "API de RSS funcionando!"}
