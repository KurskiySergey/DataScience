from exeptions import ListNumberError
from wrappers import try_warning
from re import match


class InteractiveList(list):

    @try_warning(ListNumberError)
    def ask_param(self):
        info = input("Enter list param: ")
        if match("\D", info):
            raise ListNumberError

        self.append(float(info))

    def start(self, length=5):
        while len(self) < length:
            self.ask_param()


if __name__ == "__main__":
    int_list = InteractiveList()
    int_list.start(length=2)
    print(int_list)

