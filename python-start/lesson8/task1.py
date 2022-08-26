from datetime import datetime
from wrappers import try_warning


class Data:
    format = "%d-%m-%Y"

    @classmethod
    def set_date_format(cls, new_format):
        cls.format = new_format

    @classmethod
    @try_warning(ValueError)
    def get_data_args(cls, data: str):
        data = datetime.strptime(data, cls.format)
        return data.day, data.month, data.year


if __name__ == "__main__":
    date_1 = "10-34-12"
    date_2 = "10-12-2022"
    tmp_format = "%Y-%m-%d"
    date = Data()
    args = date.get_data_args(data=date_1)
    print(args)
    args = date.get_data_args(data=date_2)
    print(args)
    date.set_date_format(new_format=tmp_format)
    print(date.get_data_args(data=date_2))
    