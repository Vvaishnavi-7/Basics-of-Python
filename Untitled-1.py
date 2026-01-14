class singletonMeta(type):
    _instances={}

    def __call__(cls,*args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls]=super().__call__(*args,**kwargs)

class logger(metaclass=singletonMeta):
    def __init__(self, filename):
        self.filename=filename

    def log(self, message):
        with open(self.filename, "a") as f:
            f.write(message+"\n")
        print(f"Logged: {message}")
logger1=logger("app.log")
logger2=logger("app.log")

logger1.log("This is first message")
logger2.log("This is second message")

print(logger1 is logger2)