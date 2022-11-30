import conteners as cont
import timeout
import random
# import exchanger as ex


class Machine:

    _access_flag: bool

    def __init__(self):
        # Initialize the new instance
        self._access_flag = False  # Flag for checking if service can have access to machine etc.
        self._products = cont.Products()  # Initialize used containers like dictionary classes
        self._currencies = cont.Currencies()
        self._money = cont.StoredMoney()

    @property
    def access_flag(self):
        return self._access_flag

    @access_flag.setter
    def access_flag(self, value):
        self._access_flag = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value

    @property
    def currencies(self):
        return self._currencies

    @currencies.setter
    def currencies(self, value):
        self._currencies = value

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        self._products = value

    def check_balance(self):  # method checking machine stored money state
        if self._money:  # check if not empty
            for value in self.money.values():
                if value != 0:
                    return True
            return False
        else:
            return False

    @staticmethod
    def input_method(name, value):
        return input("Input {}: ".format(name)), input("Input {}: ".format(value))  # default input method

    @timeout.timeout(60)
    def service_task(self):  # method allowing change machine properties
        print("You have 60 sek.\n")
        password = random.randint(0, 9)  # generate password - simplest method
        if input(str(password)) == str(password + 1):
            self.access_flag = True  # granting access
        else:
            print("Service not granted.\n")
            return 0

        which_service = input("1 - take out money\n2 - set money\n3 - update product\n4 - add currency\n")

        if which_service == "1" and self.access_flag:  # take out money
            if self.check_balance():
                buffer = self.money
                for k, v in buffer:
                    print("Withdraw: \n{}: {}.".format(k, v))
                    self.money = k, 0  # update dictionary state after withdraw
            else:
                print("Vault is empty")
            self.access_flag = False

        elif which_service == "2" and self.access_flag:  # set deposit
            self.money = self.input_method("currency name", "amount of money")
            self.access_flag = False

        elif which_service == "3" and self.access_flag:  # update product
            self.products = self.input_method("coffee name", "price")
            self.access_flag = False

        elif which_service == "4" and self.access_flag:  # add currency
            self.currencies = self.input_method("currency name", "multiplier (x*PLN)")
            self.access_flag = False

        else:
            print("Access denied.")

    def is_access_valid(self):  # run after service task to ensure access is denied
        if self.access_flag:    # because if service thread will end mid task, access wont be denied
            self.access_flag = False
            return 0
        else:
            return 0

    def default_task(self):
        for i, (k, v) in enumerate(self.products.items()):  # print enumerated products
            print(str(i) + ". " + str(k) + " " + str(v))

        coffee_case = input("Pic up a coffee by a name: ")

        if coffee_case in self.products.keys():  # pick product
            wait_confirmation = False

            while not wait_confirmation:  # pick payment option
                payment_option = input("Input Pln/Else: ")

                if payment_option == "Pln":
                    self.money.update({"Pln": self.products[coffee_case]})
                    print("Pls wait...\nDone.")
                    wait_confirmation = True

                elif payment_option == "else":
                    # url = 'https://api.exchangerate-api.com/v4/latest/USD'
                    # converter = ex.RealTimeCurrencyConverter(url)
                    # converted = converter.convert('PLN', 'USD', float(cls.products[coffeeCase].returnCost()))
                    # cls.pay("usd", converted)
                    for currencies in self.currencies.keys():
                        print(currencies)
                    currency = input("Pick currency: ")
                    converted = float(self.products[coffee_case]) * self.currencies[currency]
                    self.money.update({currency: converted})
                    print("Pls wait...\nDone.")
                    wait_confirmation = True

                else:
                    inp = input("Invalid payment. Repeat? y/n: ")
                    if inp == "n":
                        wait_confirmation = True
                    else:
                        pass
        else:
            print("Invalid coffee.")
