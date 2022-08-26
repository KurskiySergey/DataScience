from exeptions import ConfigError, ModeError
from wrappers import try_exception
from time import sleep


class TrafficLight:

    __colors = {
        "red": "\033[31m",
        "yellow": "\033[33m",
        "green": "\033[32m"
    }

    @try_exception(ConfigError)
    def __init__(self, traffic_config: dict):
        self.__config = traffic_config

        if not isinstance(self.__config, dict):
            raise ConfigError(message="Not a dictionary")

        self.__color = self.__config.get("start")
        if self.__color is None:
            raise ConfigError(message="No start color in config")

        self.__mode = self.__config.get("mode")
        if self.__mode is None or not isinstance(self.__mode, list):
            raise ConfigError(message="Wrong mode format. Should be a list of colors")

        if self.__color not in self.__mode:
            raise ConfigError(message="Start color not in mode list")

        self.__time_info = self.__config.get("color_time")
        if self.__time_info is None or self.__color not in self.__time_info.keys():
            raise ConfigError(message="Wrong time info or start color not exist in a timer dictionary")

    @staticmethod
    def __color_wrap(color):
        wrap = TrafficLight.__colors.get(color)
        if wrap is not None:
            return f"{wrap}{color}\033[39m"

        return color

    @try_exception(ModeError)
    def run(self):
        used_colors = list(self.__time_info.keys())
        current_idx = used_colors.index(self.__color)
        while True:
            print(TrafficLight.__color_wrap(self.__color))
            current_idx = current_idx + 1 if current_idx < len(used_colors)-1 else 0

            if current_idx >= len(self.__mode) or self.__mode[current_idx] != used_colors[current_idx]:
                raise ModeError(message="Exception in mode")

            sleep(self.__time_info.get(self.__color))
            self.__color = used_colors[current_idx]


if __name__ == "__main__":
    config = {
        "start": "red",
        "mode": ["red", "yellow", "green"],
        "color_time": {
            "red": 7,
            "yellow": 2,
            "green": 5,
        }
    }

    light = TrafficLight(traffic_config=config)
    light.run()
