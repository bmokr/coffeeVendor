# Module with overwritten dict to store things
# Containers !
class StoredMoney(dict):  # stored money
    def __setitem__(self, key, value):
        try:  # check if input value is float and if it's in x.xx format
            if not (isinstance(value, float) and len(str(value).split('.')[-1]) == 2):
                raise ValueError
            else:
                super().__setitem__(key, value)
        except ValueError:
            print("Value error, must be a float x.xx type")
            pass


class Products(dict):  # known coffee types and price
    def __setitem__(self, key, value):
        super().__setitem__(key, value)


class Currencies(dict):  # known multipliers
    def __setitem__(self, key, value):
        key = key.capitalize()  # uppercase first letter
        super().__setitem__(key, value)
