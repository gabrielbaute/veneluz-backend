from uuid import UUID
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict

from app.enums import FailCause, EventType

class ElectricEventCreate(BaseModel):
    """
    Modelo de registro de un nuevo evento eléctrico.

    Attributes:
        id (UUID): ID de registro de la falla/evento eléctrico.
        start_timestamp (datetime): Marca de tiempo de inicio del evento.
        end_timestamp (Optional[datetime]): Marca de tiempo de finalización del evento.
        location (str): Coordenadas desde las que se registró el evento.
        event_type (EventType): Tipo de evento, corte o fluctuación.
        fail_cause (FailCause): Tipo de causa de la falla/corte.
    """
    id: UUID
    start_timestamp: datetime
    end_timestamp: Optional[datetime] = None
    location: str
    event_type: EventType = EventType.CORTE
    fail_cause: FailCause = FailCause.DESCONOCIDA

    model_config = ConfigDict(from_attributes=True)

class ElectricEventUpdate(BaseModel):
    """
    Modelo de edición de un evento eléctrico.

    Attributes:
        start_timestamp ( Optional[datetime]): Marca de tiempo de inicio del evento.
        end_timestamp (Optional[datetime]): Marca de tiempo de finalización del evento.
        location (Optional[str]): Coordenadas desde las que se registró el evento.
        event_type (Optional[EventType]): Tipo de evento, corte o fluctuación.
        fail_cause (Optional[FailCause]): Tipo de causa de la falla/corte.
    """
    start_timestamp: Optional[datetime] = None
    end_timestamp: Optional[datetime] = None
    location: Optional[str] = None
    event_type: Optional[EventType] = None
    fail_cause: Optional[FailCause] = None

    model_config = ConfigDict(from_attributes=True)

class ElectricEventResponse(BaseModel):
    """
    Modelo de respuesta del registro de un evento eléctrico.

    Attributes:
        id (UUID): ID de registro de la falla/evento eléctrico.
        start_timestamp (datetime): Marca de tiempo de inicio del evento.
        end_timestamp (Optional[datetime]): Marca de tiempo de finalización del evento.
        location (str): Coordenadas desde las que se registró el evento.
        event_type (EventType): Tipo de evento, corte o fluctuación.
        fail_cause (FailCause): Tipo de causa de la falla/corte.
    """
    id: UUID
    start_timestamp: datetime
    end_timestamp: Optional[datetime] = None
    location: str
    event_type: EventType
    fail_cause: FailCause

    model_config = ConfigDict(from_attributes=True)

class ElectricEventListResponse(BaseModel):
    """
    Respuesta de lista de varios eventos eléctricos. Para consultas masivas en la base de datos.

    Attributes:
        events (List[ElectricEventResponse]): Lista de objetos ElectricEventResponse
        count (int): Total de eventos traídos desde la base de datos.
    """
    events: List[ElectricEventResponse] = []
    count: int = 0
