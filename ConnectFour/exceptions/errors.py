class GameError(Exception):
    def __init__(self,msg):
        self._msg = msg

    def __str__(self):
        return "Game Error: "+ str(self._msg)