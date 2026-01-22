from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Criar aplicação FastAPI
app = FastAPI(
    title="Legal AI Backend v2.0",
    description="Sistema jurídico de análise com IA",
    version="2.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check
@app.get("/api/v2/health")
async def health_check():
    """Verificar saúde do sistema"""
    return {
        "status": "healthy",
        "version": "2.0.0",
        "service": "Legal AI Backend"
    }

# Raiz
@app.get("/")
async def root():
    """Raiz da API"""
    return {
        "message": "Legal AI Backend v2.0",
        "docs": "/docs",
        "health": "/api/v2/health"
    }

# Tratamento de erros global
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Erro não tratado: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Erro interno do servidor", "detail": str(exc)}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
