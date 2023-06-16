import logging
from logging.handlers import RotatingFileHandler


class Log:


    def __init__(self, path=None, logic='OR', file_mode='a', max_bytes=0, backup_count=0):

        # Set up the logger with a formatter
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)

        # Set up a handler for the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter('%(levelname)s: %(message)s')
        console_handler.setFormatter(console_format)

        # If logging to file is needed, set up a file handler
        file_handler = None
        if path:
            file_handler = RotatingFileHandler(
                path, mode=file_mode, maxBytes=max_bytes, backupCount=backup_count,
            )
            file_handler.setLevel(logging.DEBUG)
            file_format = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
            file_handler.setFormatter(file_format)

        # Set up a logger that logs to both console and file (if set up)
        if logic == 'OR' and not file_handler:
            self.logger.addHandler(console_handler)

        elif logic == 'OR' and file_handler:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

        elif logic == 'AND' and file_handler:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

        else:
            self.logger.addHandler(console_handler)

    def __call__(self, message, level=logging.DEBUG):
        self.logger.log(level, message)