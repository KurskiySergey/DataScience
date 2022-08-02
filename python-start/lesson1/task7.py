from task1 import ask_params_from_user

if __name__ == "__main__":
    start_distance = ask_params_from_user(type_of_param="in km")
    end_distance = ask_params_from_user(type_of_param="in km")
    percent_in_day = 10
    day = 1
    result = start_distance
    if end_distance >= start_distance:
        while result < end_distance:
            result += result / 100 * percent_in_day
            day += 1
        print("\n ==== RESULT ====")
        print(f"He will run {end_distance} km on {day} day")
    else:
        print("\n ==== ERROR ====")
        print("start must be less than end distance")
