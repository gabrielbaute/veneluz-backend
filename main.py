"""
Entrypoint de la aplicación
"""
import uvicorn
from typing import AsyncGenerator
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import db_manager
from app.settings import settings, AppCustomLogger
from app.api import create_app, register_error_handlers

AppCustomLogger.setup_logging(logs_dir=settings.LOGS_DIR, level=settings.LOG_LEVEL)

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Asynchronous lifecycle manager handling application startup and shutdown tasks.

    Args:
        app (FastAPI): Active application instance context.
    """
    # Ejecuta la inicialización de la base de datos al arrancar
    await db_manager.init_db()
    yield
    # Código de limpieza/desconexión (opcional) al cerrar la aplicación

app = create_app(settings=settings, lifespan=lifespan)
register_error_handlers(app=app)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=int(settings.API_PORT),
        reload=False
    )
