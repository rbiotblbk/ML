import logging 
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


# Create/Config Logger
logger = logging.getLogger() # root logger
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s  - %(filename)s - %(name)s - %(levelname)s - %(message)s ")


# File Handler logger --> log into a file
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

# Alternative: RotationFileHandler -> File Size -> app.log.1, app.log.2, etc., max Size: 5KByte with 4x Archive Files
rotation_handler = RotatingFileHandler("app_rotate.log", maxBytes= 5000, backupCount=4)
rotation_handler.setFormatter(formatter)

# Alternative: TimeRotatingFileHandler -> Via Time
rotation_time_handler = TimedRotatingFileHandler("app_time.log", when="S", interval= 1, backupCount= 4)
rotation_time_handler.setFormatter(formatter)

# Stream(Terminal) Handler logger --> log to the terminal(console)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)




# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.addHandler(rotation_handler)
logger.addHandler(rotation_time_handler)




logger.info("Application is started...!")
logger.info("Application is finished...!")
 