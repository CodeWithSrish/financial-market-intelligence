from app.logging.logger import get_logger

logger = get_logger(__name__)

logger.debug("Debug message")

logger.info("Pipeline started")

logger.warning("API key missing")

logger.error("Download failed")

logger.critical("Pipeline stopped")