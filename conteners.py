# Module with overwritten dict to store things
# Containers !
# Tutorial: https://realpython.com/inherit-python-dict/#inheriting-from-the-python-built-in-dict-class

default_products = {  # set of default products
    "coffee": 12
}

default_currencies = {  # set of default currencies
    "Pln": 1,
    "Usa": 4.4
}


class StoredMoney(dict):  # stored money
    def __setitem__(self, key, value):
        try:  # check if input value is float and if it's in x.xx format
            if not len(str(value).split('.')[-1]) == 2:
                raise ValueError
            else:
                key = key.capitalize()  # uppercase first letter
                super().__setitem__(key, value)
        except ValueError:
            print("Value error, must be a float x.xx type")
            pass


class Products(dict):  # known coffee types and price
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __init__(self):  # initialize with default
        for key, value in default_products.items():
            self.__setitem__(key, value)


class Currencies(dict):  # known multipliers
    def __setitem__(self, key, value):
        key = key.capitalize()  # uppercase first letter
        super().__setitem__(key, value)

    def __init__(self):  # initialize with default
        for key, value in default_currencies.items():
            self.__setitem__(key, value)
