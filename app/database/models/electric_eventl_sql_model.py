from threading import Event
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

from app.enums import FailCause, EventType

class ElectricEventSQLModel(SQLModel, table=True):
    """
    Modelo de representación en la base de datos de un evento eléctrico.

    Attributes:
        id (UUID): ID de registro de la falla/evento eléctrico.
        start_timestamp (datetime): Marca de tiempo de inicio del evento.
        end_timestamp (datetime): Marca de tiempo de finalización del evento.
        location (str): Coordenadas desde las que se registró el evento.
        event_type (EventType): Tipo de evento, corte o fluctuación.
        fail_cause (FailCause): Tipo de causa de la falla/corte.
    """
    __tablename__ = "fails"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    start_timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False,)
    end_timestamp: datetime = Field(nullable=True)
    location: str = Field(nullable=False)
    event_type: EventType = Field(default=EventType.CORTE)
    fail_cause: FailCause = Field(default=FailCause.DESCONOCIDA)
