from typing import List

from .rust_chat_message import RustChatMessage
from .rust_team_info import RustTeamInfo


class Item:
    def __init__(self, app_message) -> None:
        self._itemId: int = app_message.itemId
        self._quantity: int = app_message.quantity
        self._itemIsBlueprint: bool = app_message.itemIsBlueprint

    @property
    def item_id(self) -> int:
        return self._itemId

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def item_is_blueprint(self) -> bool:
        return self._itemIsBlueprint

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise Exception("Cannot Re-Set Values")


class TeamEvent:
    def __init__(self, app_message) -> None:
        self._playerId: int = app_message.broadcast.teamChanged.playerId
        self._teamInfo = RustTeamInfo(app_message.broadcast.teamChanged.teamInfo)

    @property
    def player_id(self) -> int:
        return self._playerId

    @property
    def team_info(self) -> RustTeamInfo:
        return self._teamInfo

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise Exception("Cannot Re-Set Values")


class ChatEvent:
    def __init__(self, app_message) -> None:
        self._message = RustChatMessage(app_message.broadcast.teamMessage.message)

    @property
    def message(self) -> RustChatMessage:
        return self._message

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise Exception("Cannot Re-Set Values")


class EntityEvent:
    def __init__(self, app_message, entity_type) -> None:
        self._type = int(entity_type)
        self._entity_id: int = app_message.broadcast.entityChanged.entityId
        self._value: bool = app_message.broadcast.entityChanged.payload.value
        self._capacity: int = app_message.broadcast.entityChanged.payload.capacity
        self._hasProtection: bool = (
            app_message.broadcast.entityChanged.payload.hasProtection
        )
        self._protectionExpiry: int = (
            app_message.broadcast.entityChanged.payload.protectionExpiry
        )

        self._items: List[Item] = [
            Item(item) for item in app_message.broadcast.entityChanged.payload.items
        ]

    @property
    def type(self) -> int:
        return self._type

    @property
    def entity_id(self) -> int:
        return self._entity_id

    @property
    def value(self) -> int:
        return self._value

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def has_protection(self) -> bool:
        return self._hasProtection

    @property
    def protection_expiry(self) -> int:
        return self._protectionExpiry

    @property
    def items(self) -> List[Item]:
        return self._items

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise Exception("Cannot Re-Set Values")
