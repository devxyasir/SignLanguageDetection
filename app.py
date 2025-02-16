from signLanguage.logger import logging
from signLanguage.exceptions import SignException
import sys


logging.info("This is a test log message")

try:
    raise ValueError("This is a test exception")
except Exception as e:
    raise SignException("This is a test exception", sys)