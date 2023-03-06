import logging 

logger = logging.getLogger()

class Car:
    def __init__(self, kz) -> None:
        self.kz = kz

        logger.debug("Instance of Car is created")

    def __repr__(self) -> str:
        return f"KZ: {self.kz}"
    

