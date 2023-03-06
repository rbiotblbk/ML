import logging 
import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


# Create/Config Logging
logging.basicConfig(filename = "app.log" , level = logging.ERROR,
                    format = "%(asctime)s  - %(filename)s - %(name)s - %(levelname)s - %(message)s ")



def add(x, y):
    total  = x + y
    
    logging.debug(f"{x}, {y} -> zwischen ergebnis:{total}")

    return total

 



total = add(4,5)
print("Total:", total)

# Logging Levels
logging.debug("This is a debug message")
logging.info("This is a debug message")
logging.warning("This is a debug message")
logging.error("This is a debug message")
logging.critical("This is a debug message")
logging.exception("This is a debug message")