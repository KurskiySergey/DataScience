from datetime import timedelta
from task1 import ask_params_from_user


def custom_converter(sec: int):
    min_in_hour = 60
    sec_in_min = 60

    total_min = sec // sec_in_min
    total_h = total_min // min_in_hour
    current_data = [total_min - total_h * min_in_hour,
                    sec - total_min * sec_in_min]
    for i, data in enumerate(current_data):
        if data // 10 == 0:
            current_data[i] = f"0{data}"
    current_data = ":".join(current_data)
    info = f"{total_h}:{current_data}"
    return info


if __name__ == "__main__":
    seconds = ask_params_from_user('seconds')
    result = custom_converter(sec=seconds)
    converted_time = timedelta(seconds=seconds)
    print(f"from imported lib: {converted_time}", f"from custom func: {result}", sep="\n")

