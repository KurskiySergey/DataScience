from config import full_filename
from random import uniform


def generate_file_data(filename):
    surname_filename = "surnames.txt"
    min_salary = 10_000
    max_salary = 100_000
    with open(full_filename(surname_filename), "r", encoding="utf-8") as file:
        surnames = file.readlines()

    salary_info = [f"{surname.strip()} {round(uniform(min_salary, max_salary), 2)}\n" for surname in surnames]
    with open(full_filename(filename), "w", encoding="utf-8") as file:
        file.writelines(salary_info)


def main(filename):
    with open(full_filename(filename), "r", encoding="utf-8") as file:
        data = file.readlines()

    search_salary = 20_000
    workers = [info.strip().split(" ")[0] for info in data if float(info.strip().split(" ")[1]) < search_salary]
    avr_salary = round(sum(map(lambda x: float(x.strip().split(" ")[1]), data)) / len(data), 2)
    print(f"Workers with salary less than {search_salary}")
    print(workers)
    print(f"Average salary of all workers: ")
    print(avr_salary)


if __name__ == "__main__":
    filename = "task3.txt"
    generate_file_data(filename=filename)
    main(filename=filename)