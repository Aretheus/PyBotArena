from card import Card
from random import shuffle

class Deck:
    def __init__(self) -> None:
        self._cards: list[Card] = []

    def draw_cards(self, num: int = 1):
        drawn_cards: list[Card] = []
        for i in range(num):
            drawn_cards.append(self._cards.pop(0))
        return drawn_cards

    def shuffle(self) -> None:
        shuffle(self._cards)
