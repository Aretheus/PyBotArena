from enum import Enum

class Rotate(Enum):
    NONE = 0
    LEFT = 1
    UTURN = 2
    RIGHT = 3

class Card:
    def __init__(self, rotation: int, move: int, priority: int) -> None:
        self.__rotate: Rotate = Rotate(rotation)
        self.__move: int = move
        self.__priority: int = priority
