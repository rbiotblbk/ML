import logging 
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

# Stream(Terminal) Handler logger --> log to the terminal(console)
stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)




logger.info("Application is started...!")
logger.info("Application is finished...!")
 