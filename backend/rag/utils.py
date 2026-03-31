import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('backend/info.log')
    ]
)

logger = logging.getLogger(__name__)

def log_error(error_msg):
    logger.error(error_msg)

def log_info(info_msg):
    logger.info(info_msg)
