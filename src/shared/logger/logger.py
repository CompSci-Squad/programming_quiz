"""Custom logger."""
from sys import stdout

from loguru import logger
   
def loguru_formatter(log):
    if log["level"].name == "WARNING":
        return "<white>{time:MM-DD-YYYY HH:mm:ss}</white> | <light-yellow>{level}</light-yellow>: <light-white>{message}</light-white> \n"
    elif log["level"].name == "ERROR":
        return "<white>{time:MM-DD-YYYY HH:mm:ss}</white> | <light-red>{level}</light-red>: <light-white>{message}</light-white> \n"
    elif log["level"].name == "SUCCESS":
        return "<white>{time:MM-DD-YYYY HH:mm:ss}</white> | <light-green>{level}</light-green>: <light-white>{message}</light-white> \n"
    else:
        return "<white>{time:MM-DD-YYYY HH:mm:ss}</white> | <fg #67c9c4>{level}</fg #67c9c4>: <light-white>{message}</light-white> \n"

def create_logger():
    """Create custom logger."""
    logger.remove()
    logger.add(stdout, colorize=True, format=loguru_formatter)
    return logger


LOGGER = create_logger()
