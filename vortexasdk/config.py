"""module level Scooby dooby"""
import os


class Config:
    """Class level dooby"""

    @property
    def LOG_LEVEL(self):
        """Log level property"""
        return os.getenv("LOG_LEVEL", "WARNING").upper()


LOG_LEVEL = "WARNING"
LOG_FILE = os.getenv("LOG_FILE", None)

HTTP_PROXY = os.getenv("HTTP_PROXY", None)
HTTPS_PROXY = os.getenv("HTTPS_PROXY", None)
