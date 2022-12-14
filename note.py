# not mine; example of well writen user-type dict-like container
DEFAULT_CURRENCIES = {
    'zł': 1,
    '$': 4.9,
    'fount': 5.2
}


class Money:

    def __init__(self) -> None:
        self._currencies = DEFAULT_CURRENCIES

    @property
    def currencies(self):
        return self._currencies

    @staticmethod
    def _check_key(key: str):
        if not isinstance(key, str):
            raise TypeError('Currency must be a str')

    def __setitem__(self, key: str, value: float):
        self._check_key(key)
        if not isinstance(value, float):
            raise TypeError('Value of the currency should be a float')
        if key in self._currencies:
            raise KeyError('Currency already used, please try again')

        self._currencies[key] = value

    def __getitem__(self, key: str):
        self._check_key(key)
        if key not in self._currencies:
            raise KeyError('Currency with this key not found')
        return self._currencies[key]


m = Money()
print(m.currencies)
print(m['zł'])
print(m['$'])
m['test'] = 2.2
print(m.currencies)
