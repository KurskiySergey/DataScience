from config import full_filename
from random import randint
import json

INCOME_MIN = 200_000
INCOME_MAX = 500_000
COSTS_MIN = 50_000
COSTS_MAX = 300_000
AMOUNT = 10


def generate_file(filename):
    lines = [f"firm_{i+1} OOO {randint(INCOME_MIN, INCOME_MAX)} {randint(COSTS_MIN, COSTS_MAX)}\n" for i in range(AMOUNT)]
    with open(full_filename(filename), "w", encoding="utf-8") as file:
        file.writelines(lines)


def main(filename, json_filename):
    firm_info = {}
    with open(full_filename(filename), "r", encoding="utf-8") as file:
        with open(full_filename(json_filename), "w", encoding="utf-8") as j_file:
            for line in file:
                name, form, income, cost = line.strip().split(" ")
                firm_info[name] = int(income) - int(cost)
            avr_profit = sum(firm_info.values())

            database = [
                firm_info,
                {"avr_profit": avr_profit}
            ]

            json.dump(database, j_file)


if __name__ == "__main__":
    filename = "task7.txt"
    json_filename = "task7.json"
    generate_file(filename=filename)
    main(filename=filename, json_filename=json_filename)