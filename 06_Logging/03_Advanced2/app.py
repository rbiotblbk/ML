import logging 
from logging.config import fileConfig
import os 
from pathlib import Path 
from car import Car

os.chdir(Path(__file__).parent)


fileConfig("logging.ini")

logger = logging.getLogger("") 

logger.info("Application is started...!")


car1 = Car("AAA12345")
print(car1)


logger.info("Application is finished...!")
 