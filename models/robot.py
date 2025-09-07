from card import Card


class Robot:
    def __init__(self) -> None:
        self.lives = 3
        self.damage: int = 0
        self.position: tuple[int, int] = (0,0)
        self.registers: list[Card] = []
        self.powerdown = False

    def update_position(self):
        pass

    def restart(self):
        # when the robot's hp reaches 0
        pass

    def takes_damage(self, dmg: int):
        # when the robot takes damage from any source, reduce the robot's health by that value
        # if the robot's hp would be reduced to below
        self.health -= dmg
