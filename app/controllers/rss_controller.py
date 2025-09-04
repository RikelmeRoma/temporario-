from fastapi.responses import JSONResponse
from app.services.rss_service import buscar_rss

def get_rss_controller():
    dados = buscar_rss()
    return JSONResponse(content=dados)
