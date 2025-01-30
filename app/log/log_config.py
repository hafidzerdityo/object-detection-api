import structlog
import logging
from datetime import date

# configure structlog
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

# set up the log file
log_file = f"log/app_{date.today()}.log"

# file handler
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# stream handler (for terminal output)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# configure root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)  # set the desired log level
root_logger.addHandler(file_handler)
root_logger.addHandler(stream_handler)

# get the structlog logger
logger = structlog.get_logger()
logger.info("Informational message")
logger.error("Error message")
