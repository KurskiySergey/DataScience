from task5 import deposit_calculator
from task1 import ask_params_from_user
if __name__ == "__main__":

    result, income, costs = deposit_calculator()
    if result:
        rent_res = (income - costs) / income
        num_workers = ask_params_from_user(type_of_param="number of workers")
        inc_per_worker = income / num_workers

        print(f"rent_res = {rent_res}\n"
              f"inc_per_worker = {inc_per_worker}")
        