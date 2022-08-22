from wrappers import try_warning
from exeptions import VelocityError


class Car:
    allowed_speed = 200

    def __init__(self, name, speed):
        self.name = name
        self.__color = "white"
        self.__speed = speed
        self.__is_police = False
        self.__is_move = False

    def make_police(self):
        self.__is_police = True

    @property
    def speed(self):
        return int(self.__speed)

    def change_color(self, new_color):
        self.__color = new_color

    def launch(self):
        print(f"Engine is launched. Machine is stoped")
        print("WASD to move, E to gas, Q to stop, C to change speed")
        while True:
            command = input().lower()

            if command == "e":
                self.go()
            if self.__is_move:
                if command == "w":
                    self.turn(direction="forward")

                if command == "a":
                    self.turn(direction="left")

                if command == "d":
                    self.turn(direction="right")

                if command == "s":
                    self.turn(direction="back")

                if command == "c":
                    velocity = input("New speed ")
                    self.change_speed(velocity=velocity)

                if command == "q":
                    self.stop()
                    break
            else:
                print("press E to gas")

    def go(self):
        self.__is_move = True
        self.turn("forward")

    def stop(self):
        self.__is_move = False
        print("Stop car")

    @try_warning(VelocityError)
    def change_speed(self, velocity):
        self.__speed = velocity
        if self.speed > self.allowed_speed:
            raise VelocityError(message=f"new speed is not allowed for this type of car.\n"
                                        f"Allowed speed is {self.allowed_speed}. Current speed = {self.speed}")

        print(f"New speed is {self.speed}")

    def turn(self, direction):
        print(f"turned to {direction}\n")
        print(f"current speed {self.speed}")


class TownCar(Car):
    allowed_speed = 60


class WorkCar(Car):
    allowed_speed = 40


class PoliceCar(Car):
    allowed_speed = 100

    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.make_police()
        self.change_color(new_color="white/blue")


class SportCar(Car):
    allowed_speed = 250


if __name__ == "__main__":
    car = TownCar(name="test", speed=50)
    car.launch()
