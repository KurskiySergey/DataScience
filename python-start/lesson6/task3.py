class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    def get_salary(self):
        return self.__income.get("wage")

    def get_bonus(self):
        return self.__income.get("bonus")


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname} ({self.position})"

    @property
    def total_income(self):
        return self.get_salary() + self.get_bonus()


if __name__ == "__main__":

    worker = Position(name="Test", surname="Test", position="test", income={"wage": 12, "bonus": 12})
    full_name = worker.get_full_name()
    print(full_name)
    print(worker.total_income)
