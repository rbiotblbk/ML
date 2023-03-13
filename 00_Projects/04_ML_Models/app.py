class DP:
    pass 


class LR:
    pass 

class LogR:
    pass


class Model:
    def __init__(self, model_type) -> None:
        match model_type:
            case "LR":
                self.model  =  LR()



mymodel = Model("LR")

