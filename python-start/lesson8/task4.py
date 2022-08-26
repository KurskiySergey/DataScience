from wrappers import try_warning
from exeptions import NoPlaceError, NoItemError
from pprint import pprint


class Technique:
    def __init__(self, idx=0, class_id=0, **kwargs):
        self.id = idx
        self.class_id = class_id
        self.add_info = kwargs

    def __repr__(self):
        return f"{self.id} {self.add_info}"

    def get_object(self, **kwargs):
        if "idx" in kwargs.keys():
            if self.id == kwargs.get("idx"):
                return self
            else:
                return None

        if "class_id" in kwargs.keys():
            if self.class_id == kwargs.get("class_id"):
                return self
            else:
                return None

        for key, value in kwargs.items():
            if self.add_info.get(key) is not None:
                if self.add_info.get(key) == value:
                    return self

        return None


class Printer(Technique):
    def __init__(self, **kwargs):
        super().__init__(class_id=0, **kwargs)

    def unique_method(self):
        print("something special for printer")


class Scaner(Technique):
    def __init__(self, **kwargs):
        super().__init__(class_id=1, **kwargs)

    def unique_method(self):
        print("something special for scaner")


class Xerox(Technique):
    def __init__(self, **kwargs):
        super().__init__(class_id=2, **kwargs)

    def unique_method(self):
        print("something special for xerox")


class StoreHouse:
    def __init__(self, capacity=100):
        self.store_info = {}
        self.class_map = {}
        self.capacity = capacity

    @try_warning(NoPlaceError)
    def push_item(self, item: Technique):
        if self.capacity <= 0:
            raise NoPlaceError()

        last_id = len(self.store_info)
        item.id = last_id
        self.store_info[last_id] = item
        self.capacity -= 1

    @try_warning(NoItemError)
    def pop_item(self, item_id):
        item = self.store_info.get(item_id)
        if item is None:
            raise NoItemError(message="Item with this id is not exist")
        self.store_info.pop(item_id)
        self.capacity += 1
        return item

    @try_warning(NoItemError)
    def find_item(self, **kwargs):
        search_item = None
        for key, item in self.store_info.items():
            if item.get_object(**kwargs) is not None:
                search_item = item
                break

        if search_item is None:
            raise NoItemError(message="No item with such data")

        return search_item

    def get_statistic(self):
        class_map = {}
        for idx, item in self.store_info.items():
            if class_map.get(item.class_id) is None:
                class_map[item.class_id] = [item]
            else:
                class_map[item.class_id].append(item)
        print(f"Left capacity: {self.capacity}")
        print("===Storage Info===")
        pprint(class_map)


if __name__ == "__main__":
    store = StoreHouse(capacity=1)
    teh = Printer(model="HP")
    store.get_statistic()
    store.push_item(teh)
    store.get_statistic()
    search_item = store.find_item(model="HP")
    store.pop_item(search_item.id)
    store.get_statistic()
