import structlog
import logging
from datetime import date


structlog.configure(
    processors=[
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
)

log_file = f"log/app_{date.today()}.log"

file_handler = logging.FileHandler(log_file)

file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))


logging.getLogger().addHandler(file_handler)

logger = structlog.get_logger()
logger.info("Informational message")
logger.error("Error message")
