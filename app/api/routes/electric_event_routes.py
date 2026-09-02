"""
Módulo para rutas de registro y consulta de eventos eléctricos.
"""
from uuid import UUID
from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, Query

from app.enums import EventType, FailCause
from app.services import ElectricEventService
from app.api.dependencies import get_electric_event_service
from app.schemas import (
    ElectricEventCreate,
    ElectricEventListResponse,
    ElectricEventResponse,
    ElectricEventUpdate
)


router = APIRouter(prefix="/events", tags=["Electric Events"])

@router.post("/register", response_model=ElectricEventResponse)
async def register_event(
    event_in: ElectricEventCreate,
    electric_event_service: ElectricEventService = Depends(get_electric_event_service)
) -> Optional[ElectricEventResponse]:
    """
    Endpoint de registro de un evento eléctrico.
    """
    electric_event = await electric_event_service.register_event(event_data=event_in)
    return electric_event

@router.put("/{event_id}", response_model=ElectricEventResponse)
async def update_event(
    event_id: UUID,
    event_data: ElectricEventUpdate,
    electric_event_service: ElectricEventService = Depends(get_electric_event_service)
) -> Optional[ElectricEventResponse]:
    """
    Actualiza un evento específico
    """
    return await electric_event_service.update_event(event_id=event_id, event_data=event_data)

@router.get("/{event_id}", response_model=ElectricEventResponse)
async def get_event_by_id(
    event_id: UUID,
    electric_event_service: ElectricEventService = Depends(get_electric_event_service)
) -> Optional[ElectricEventResponse]:
    """
    Obtiene el detalle de un evento.
    """
    return await electric_event_service.get_event_by_id(event_id=event_id)

@router.get("/history", response_model=ElectricEventListResponse)
async def get_history_events(
    start_date: datetime = Query(description="Fecha de inicio (YYYY-MM-DDTHH:MM:SS)."),
    end_date: datetime = Query(description="Fecha de fin mas reciente (YYYY-MM-DDTHH:MM:SS)."),
    skip: int = Query(0, ge=0, description="Registros a saltar (paginación)."),
    limit: int = Query(100, ge=1, le=1000, description="Cantidad máxima de registros a solicitar."),
    electric_event_service: ElectricEventService = Depends(get_electric_event_service)
) -> ElectricEventListResponse:
    """
    Obtiene el histórico de eventos eléctricos para un rango de tiempo dado.
    """
    event_records = await electric_event_service.get_events_by_date_range(
        start_date=start_date,
        end_date=end_date,
        skip=skip,
        limit=limit
    )
    return event_records
