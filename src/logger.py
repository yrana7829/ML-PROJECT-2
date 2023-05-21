import logging
import os
from datetime import datetime


# Create a text file with a name convention
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# define path for this file
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# Now implement the logging message

# The log messages will be formatted according to the provided format string, which includes the timestamp, line number, logger name, log level, and log message

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]%(lineno)d%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Check if the logging has started

# if __name__ == "__main__":
#     logging.info('Confratulations Logging has started')
