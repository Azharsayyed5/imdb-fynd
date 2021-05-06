import os
import sys
import logging
from datetime import date

LOG_DIRECTORY = "/var/log/"
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def logging_handler():
    
    today = date.today()

    filename = f"root.logs.{today.strftime('%d-%m-%Y')}"
    if not os.path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY)

    # Initialize directory and formatter
    logging.basicConfig(
        filename=LOG_DIRECTORY + filename + ".txt", format=LOG_FORMAT, filemode='w'
        )

    # Creating an object
    logger=logging.getLogger()
    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    # add ch to logger
    return logger