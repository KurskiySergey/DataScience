first_param = 0
second_param = 3
third_param = "hello world"


def ask_params_from_user(type_of_param: str = None):
    input_string = "Write your param here"
    update_string = f"{input_string}: " if type_of_param is None else f"{input_string} in {type_of_param}: "
    user_param = input(update_string)
    print(type(user_param), user_param)
    try:
        user_param = int(user_param)
        print("Converted to int")
    except ValueError:
        print("Error while converting.\n"
              "Return origin string")

    return user_param


if __name__ == "__main__":

    input_values = [ask_params_from_user() for _ in range(first_param, second_param)]
    print(first_param, second_param, third_param)
    print(input_values)

