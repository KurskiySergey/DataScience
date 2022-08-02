from task1 import ask_params_from_user


def custom_func(str_value: str):

    length = len(str_value)
    max_value = int(str_value[length-1])
    while length > 0:
        if int(str_value[length-1]) > max_value:
            max_value = int(str_value[length-1])
        length -= 1

    return max_value


if __name__ == "__main__":
    number = ask_params_from_user(type_of_param="int")
    if number > 0:
        str_number = str(number)
        max_value = max(str_number, key=lambda x: int(x))
        print(max_value, custom_func(str_number))
    else:
        print("not positive number")
