from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--name", "-n", type=str, help="Name of the worker", default="User")
parser.add_argument("--salary", "-s", type=float, help="Salary of the current worker", default=27)
parser.add_argument("--time", "-t", type=int, help="Time of work", default=720)
parser.add_argument("--premium", "-p", type=float, help="Premium of the worker", default=2_000)
args = parser.parse_args()


def get_salary_of_worker(salary, time, premium):
    return salary * time + premium


if __name__ == "__main__":
    worker_salary = get_salary_of_worker(salary=args.salary, time=args.time, premium=args.premium)
    print(worker_salary)
