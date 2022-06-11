class Singleton:
    _instance = None

    def __init__(self):
        self.some_value = None

    @classmethod
    def get_instance(msg):
        if msg._instance is None:
            msg._instance = msg()
        return msg._instance