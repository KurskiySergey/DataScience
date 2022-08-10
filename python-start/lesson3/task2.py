
def user_info(name, year, city, email, phone):
    values = locals()
    string_res = "\n".join([f"{key}: {value}" for key, value in values.items()])
    print(string_res)


if __name__ == "__main__":
    user_info(name="test", year=1990, city="Moscow", email="test@mail.ru", phone="9999999999")