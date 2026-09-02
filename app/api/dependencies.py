"""
API Inversion of Control and Dependency Injection Module.

This module encapsulates initialization graphs for operational database sessions,
centralized configurations, and business core services inside the API route lifecycles.
"""
from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.settings.app_settings import Settings, settings
from app.database.database_manager import DatabaseManager, db_manager
from app.services.electric_events_service import ElectricEventService

def get_settings_instance() -> Settings:
    """
    Provide the globally instantiated configuration state.

    Returns:
        Settings: App configuration containing environments managed by Pydantic.
    """
    return settings


def get_db_manager() -> DatabaseManager:
    """
    Provide the structural database manager instance.

    Returns:
        DatabaseManager: Centralized connection and pooling orchestrator instance.
    """
    return db_manager

async def get_db_session(
    db_manager: DatabaseManager = Depends(get_db_manager)
) -> AsyncGenerator[AsyncSession, None]:
    """
    Genera y gestiona el ciclo de vida de una sesión de base de datos transaccional aislada.

    Utiliza una estructura de generador asíncrono para ceder el control de forma segura a las operaciones de la API posteriores
    y garantizar la liberación estricta de recursos al finalizar.

    Args:
        db_mngr (DatabaseManager): Referencia de mapeo del motor de base de datos multipool.

    Returns:
        AsyncGenerator[AsyncSession, None]: Canalización transaccional activa dirigida a las capas de almacenamiento SQLite.
    """
    async for session in db_manager.get_session():
        yield session


async def get_electric_event_service(
    database_session: AsyncSession = Depends(get_db_session)
) -> ElectricEventService:
    """
    Provee una isntancia del servicio de registro de eventos eléctricos.
    """
    return ElectricEventService(database_session=database_session)
