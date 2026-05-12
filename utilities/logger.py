"""
Logger Module
==============
Provides centralized logging for the test framework.
Logs are written to both console and a timestamped log file in the logs/ directory.
"""

import logging
import os
from datetime import datetime


class Logger:
    """
    Centralized logging utility for the test framework.
    Creates a single logger instance shared across the entire framework.
    """

    _logger = None

    @classmethod
    def get_logger(cls):
        """
        Get or create the framework logger.

        Returns:
            logging.Logger: Configured logger instance
        """
        if cls._logger is None:
            cls._logger = logging.getLogger("SauceDemo_Automation")
            cls._logger.setLevel(logging.DEBUG)

            # Create logs directory if it doesn't exist
            log_dir = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                "logs"
            )
            os.makedirs(log_dir, exist_ok=True)

            # File handler - logs everything to a file
            log_file = os.path.join(
                log_dir,
                f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
            )
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setLevel(logging.DEBUG)

            # Console handler - logs INFO and above to console
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # Log message format
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers to logger
            cls._logger.addHandler(file_handler)
            cls._logger.addHandler(console_handler)

        return cls._logger
