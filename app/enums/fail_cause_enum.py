"""Módulo para la representación de los tipos de corte eléctrico."""
from enum import StrEnum
from typing import Optional

class FailCause(StrEnum):
    """
    Tipo de corte eléctrico en función de su causa.

    Attributes:
        FALLA (str): Corte por falla eléctrica local o regional, no intencional.
        RACIONAMIENTO (str): Corte eléctrico por racionamiento.
        MANTENIMIENTO (str): Para realizar algún mantenimiento local o regional.
        DESCONOCIDA (str): Se desconoce el motivo del corte eléctrico.
        NO_APLICA (str): Cuando no se trata de un corte sino de una fluctuación.
    """
    FALLA = "FALLA"
    RACIONAMIENTO = "RACIONAMIENTO"
    MANTENIMIENTO = "MANTENIMIENTO"
    DESCONOCIDA = "DESCONOCIDA"
    NO_APLICA = "NO_APLICA"

    @staticmethod
    def from_string(fail_type: str) -> Optional['FailType']:
        fail_types: dict[str, FailType] = {
            "falla": FailType.FALLA,
            "racionamiento": FailType.RACIONAMIENTO,
            "mantenimiento": FailType.MANTENIMIENTO,
            "desconocida": FailType.DESCONOCIDA,
            "no_aplica": FailType.NO_APLICA
        }
        try:
            return fail_types.get(fail_type.strip())
        except Exception as e:
            raise ValueError(f"Unsuported type: {e}")
