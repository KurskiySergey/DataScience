from abc import ABC, abstractmethod


class Stationery(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def draw(self):
        pass


class Pen(Stationery):

    def __init__(self):
        super().__init__(title="pen")

    def draw(self):
        print("pen draw")


class Pencil(Stationery):

    def __init__(self):
        super().__init__(title="pencil")

    def draw(self):
        print("pencil draw")


class Handle(Stationery):

    def __init__(self):
        super().__init__(title="handle")

    def draw(self):
        print("handle draw")


if __name__ == "__main__":
    pen = Pen()
    pencil = Pencil()
    handle = Handle()

    pencil.draw()
    pen.draw()
    handle.draw()
