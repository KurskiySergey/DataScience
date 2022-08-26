from pprint import pprint

if __name__ == "__main__":
    data = [
        (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
        (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
        (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
    ]

    output_data = {
        key: set([info[1].get(key) for info in data]) for key in data[0][1].keys()
    }

    pprint(output_data)