"""Módulo para la representación de los tipos de fallo eléctrico."""
from enum import StrEnum
from typing import Optional

class EventType(StrEnum):
    """
    Tipo de evento eléctrico.

    Attributes:
        CORTE (str): Corte eléctrico.
        CAIDA_TENSION (str): Caída de la tensión eléctrica en la red, sin que la electricidad se corte por completo.
        FLUCTUACION (str): Fluctuación o pico en la red eléctrica.
    """
    CORTE = "CORTE"
    CAIDA_TENSION = "CAIDA_TENSION"
    FLUCTUACION = "FLUCTUACION"

    @staticmethod
    def from_string(event_type: str) -> Optional['EventType']:
        event_types: dict[str, EventType] = {
            "corte": EventType.CORTE,
            "caida_tension": EventType.CAIDA_TENSION,
            "fluctuacion": EventType.FLUCTUACION
        }
        try:
            return event_types.get(event_type.strip())
        except Exception as e:
            raise ValueError(f"Unsuported type: {e}")
