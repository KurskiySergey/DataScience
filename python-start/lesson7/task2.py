from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, var):
        self.var = var

    @abstractmethod
    def consumption(self):
        return self.var


class Coat(Clothes):
    def __init__(self, size):
        super().__init__(var=size)

    @property
    def consumption(self):
        return self.var / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        super().__init__(var=height)

    @property
    def consumption(self):
        return 2 * self.var + 0.3


if __name__ == "__main__":
    coat = Coat(size=10)
    costume = Costume(height=10)

    print(coat.consumption)
    print(costume.consumption)