class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        brace1 = "{"
        brace2 = "}"
        return f"{brace1}Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}{brace2}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        elif self.hidden is True:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if isinstance(other, Herbivore):
            if other.hidden is False:
                other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
