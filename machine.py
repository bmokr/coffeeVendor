import conteners as cont
import random
# import exchanger as ex
import exit_deco


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

    def check_balance(self):  # method checking machine stored money state
        if self._money:  # check if not empty
            for value in self._money.values():
                if value != 0:
                    return True
            return False
        else:
            return False

    @staticmethod
    def input_method(name, value):
        return input("Input {}: ".format(name)), input("Input {}: ".format(value))  # default input method

    def auth(self):
        password = random.randint(0, 9)  # generate password - simplest method
        if input(str(password)) == str(password + 1):
            self.access_flag = True  # granting access
            return 1
        else:
            print("Service not granted.\n")
            self.access_flag = False
            return 0

    @exit_deco.exit_after(60)
    def service_task(self):  # method allowing change machine properties

        if self.auth():
            print("You have 60 sek.\n")

            which_service = input("1 - take out money\n2 - set money\n3 - update product\n4 - add currency\n")

            if which_service == "1" and self.access_flag:  # take out money
                if self.check_balance():
                    for k, v in self._money.items():
                        print("Withdraw: \n{}: {}.".format(k, v))
                        self._money = k, "0.00"  # update dictionary state after withdraw
                else:
                    print("Vault is empty")
                self.access_flag = False

            elif which_service == "2" and self.access_flag:  # set deposit
                self._money = self.input_method("currency name", "amount of money")
                self.access_flag = False

            elif which_service == "3" and self.access_flag:  # update product
                self._products = self.input_method("coffee name", "price")
                self.access_flag = False

            elif which_service == "4" and self.access_flag:  # add currency
                self._currencies = self.input_method("currency name", "multiplier (x*PLN)")
                self.access_flag = False

        else:
            print("Access denied.")

    def is_access_valid(self):  # run after service task to ensure access is denied
        if self.access_flag:    # because if service thread will end mid task, access wont be denied
            self.access_flag = False
            return 0
        else:
            return 0

    def service_for_user(self):  # method for user usage
        self.service_task()
        self.is_access_valid()

    def default_task(self):
        for i, (k, v) in enumerate(self._products.items()):  # print enumerated products
            print(str(i) + ". " + str(k) + " " + str(v))

        coffee_case = input("Pic up a coffee by a name: ")

        if coffee_case in self._products.keys():  # pick product
            wait_confirmation = False

            while not wait_confirmation:  # pick payment option
                payment_option = input("Input Pln/Else: ")

                if payment_option == "Pln":
                    self._money.update({"Pln": self._products[coffee_case]})
                    print("Pls wait...\nDone.")
                    wait_confirmation = True

                elif payment_option == "Else":
                    # url = 'https://api.exchangerate-api.com/v4/latest/USD'
                    # converter = ex.RealTimeCurrencyConverter(url)
                    # converted = converter.convert('PLN', 'USD', float(cls.products[coffeeCase].returnCost()))
                    # cls.pay("usd", converted)
                    for currencies in self._currencies.keys():
                        print(currencies)
                    currency = input("Pick currency: ")
                    converted = float(self._products[coffee_case]) * self._currencies[currency]
                    self._money.update({currency: converted})
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
