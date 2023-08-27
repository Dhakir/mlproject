
import logging
import sys
from logger import datetime

from exception import CustomException

try:
    a=1/0
except Exception as e:
    logging.critical("Hello")
    a= CustomException("A Division by zero",sys)
