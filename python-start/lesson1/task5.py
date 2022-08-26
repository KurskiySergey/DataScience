from task1 import ask_params_from_user


def deposit_calculator():
    try:
        income = float(ask_params_from_user(type_of_param="your income in rub"))
        costs = float(ask_params_from_user(type_of_param="your costs in rub"))
        print("\n===== RESULT =====")
        result = True if income - costs > 0 else False
        if result:
            print("Clear plus")
        else:
            print("You are in minus")
        return result, income, costs

    except ValueError:
        print("Wrong input data.")


if __name__ == "__main__":
    deposit_calculator()
