# Module with overwritten dict to store things
# Containers !
class StoredMoney(dict):
    def __setitem__(self, key, value):
        try:  # check if input value is float and if it's in x.xx format
            if not (isinstance(value, float) and len(str(value).split('.')[-1]) == 2):
                raise ValueError
            else:
                super().__setitem__(key, value)
        except ValueError:
            print("Value error, must be a float x.xx type")
            pass


class Products(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)


class Currencies(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
