class RustChatMessage:
    def __init__(self, data):
        self._steamId: int = data.steamId
        self._name: str = data.name
        self._message: str = data.message
        self._colour: str = data.color
        self._time: int = data.time

    @property
    def steam_id(self) -> int:
        return self._steamId

    @property
    def name(self) -> str:
        return self._name

    @property
    def message(self) -> str:
        return self._message

    @property
    def colour(self) -> str:
        return self._colour

    @property
    def time(self) -> int:
        return self._time

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise Exception("Cannot Re-Set Values")

    def __repr__(self):
        return "RustChatMessage[steamId={}, senderName={}, message={}, colour={}, time={}]".format(
            self.steam_id, self._name, self._message, self._colour, self._time
        )
