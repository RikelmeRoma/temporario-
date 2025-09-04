from fastapi import APIRouter
from app.services.rss_service import buscar_e_converter_rss_para_json
from fastapi.responses import JSONResponse
from app.controllers.rss_controller import router as rss_router

router = APIRouter(
    prefix="/rss",  # agora todas as rotas começam com /rss
    tags=["RSS"]
)

@router.get("/")
def get_rss():
    dados = buscar_e_converter_rss_para_json()
    return JSONResponse(content=dados)
