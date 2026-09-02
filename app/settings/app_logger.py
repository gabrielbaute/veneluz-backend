import logging
from pathlib import Path
from typing import Dict, Optional
from logging.handlers import RotatingFileHandler

class FixedWidthFormatter(logging.Formatter):
    """
    Formatter that ensures a fixed width for the levelname.
    """
    def __init__(self, fmt=None, datefmt=None, level_width=8):
        super().__init__(fmt, datefmt)
        self.level_width = level_width

    def format(self, record):
        # We format the levelname with fixed width and left justification
        record.levelname = record.levelname.ljust(self.level_width)
        return super().format(record)

class AppCustomLogger:
    """
    Log system configuration.
    """
    # Parámetros de rotación: 5MB por archivo, manteniendo hasta 5 backups
    MAX_BYTES: int = 5 * 1024 * 1024
    BACKUP_COUNT: int = 5
    LEVEL_MAP: Dict[str, int] = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    @staticmethod
    def setup_logging(logs_dir: Path, level: Optional[str] = "INFO") -> None:
        """
        Configura el sistema de logging básico.

        Args:
            logs_dir (Path): Directorio donde se guardarán los logs.
            level (Optional[str]): Nivel de registro. Ejemplo: "DEBUG", "INFO", etc.

        Returns:
            None
        """
        if not logs_dir.exists():
            logs_dir.mkdir(parents=True, exist_ok=True)

        log_file: Path = logs_dir / "veneluz_server.log"
        log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

        rotate_handler = RotatingFileHandler(
            filename=str(log_file),
            mode="a",
            maxBytes=AppCustomLogger.MAX_BYTES,
            backupCount=AppCustomLogger.BACKUP_COUNT,
            encoding="utf-8"
        )
        stream_handler = logging.StreamHandler()

        formatter = FixedWidthFormatter(
            fmt=log_format,
            datefmt="%Y-%m-%d %H:%M:%S",
            level_width=8
        )

        rotate_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        root_logger = logging.getLogger()
        root_logger.setLevel(AppCustomLogger.LEVEL_MAP.get(str(level), logging.INFO))

        root_logger.handlers.clear()

        root_logger.addHandler(rotate_handler)
        root_logger.addHandler(stream_handler)
