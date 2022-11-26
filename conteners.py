# Module with overwritten dict to store things
# Containers !
class StoredMoney(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)


class Products(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)


class Currencies(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
