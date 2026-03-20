import logging


class LoggerConfig:
    LOGS_DIR_NAME = "logs"
    LOGGER_NAME = "TestFramework"
    LOGS_FILE_NAME = f"{LOGS_DIR_NAME}/test.log"
    LOGS_LEVEL = logging.INFO
    MAX_BYTES = 100000          # ← изменено
    BACKUP_COUNT = 10           # ← изменено
    FORMAT = "[%(asctime)s - %(levelname)s] - %(message)s"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
