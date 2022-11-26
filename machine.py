import product as p
import conteners as cont
import timeout
import curr as c
# import exchanger as ex

class Machine:
    _access_flag: bool

    def __init__(self):
        # Initialize the new instance
        self._access_flag = False  # Flag for checking if service can have access to machine etc.
        self.products = cont.Products()  # Initialize used containers like dictionaries classes
        self.currencies = cont.Currencies()
        self.money = cont.StoredMoney()

    @property
    def access_flag(self):
        return self._access_flag

    @access_flag.setter
    def access_flag(self, value):
        self._access_flag = value




    def checkBalance(self):
        for value in self.money.values():
            if value != 0:
                return True
        return False

    def moneyGet(self, password):
        if password and self.checkBalance():
            for k, v in self.money.items():
                print("Withdraw: \n{}: {}.".format(k, v))
                self.money.update({k: 0})
        else:
            if not password:
                print("Access denied.")
            else:
                print("No money.")

    def moneySet(self, password, pln, usd):
        if password:
            self.money.update({"pln": pln, "usd": usd})
            print("Machine deposit is now updated.")
        else:
            print("Access denied.")

    def pay(self, name, value):
        self.money.update({name: float(value) + float(self.money[name])})

    def getProducts(self, name):  # get product price
        return self.products.get(name)

    def setProducts(self, password):  # update or set product
        if password:
            name = input("Input product name: ")
            ingredients = input("Input product ingredients (like *, *): ")
            cost = input("Input product cost: ")
            self.products.update({name: p.Product(ingredients, cost)})
        else:
            print("Access denied.")

    def getCoefficient(self, name):  # get currency coefficient
        return self.currencies.get(name)

    def setCoefficient(self, password):
        if password:
            name = input("Input currency name: ")
            coefficient = input("Input currency coefficient: ")
            self.currencies.update({name: c.Currency(coefficient)})
            self.money.update({name: 0})
        else:
            print("Access denied.")

    @timeout.timeout(60)
    def service_task(self, is_access):  # method allowing change machine properties
        which_service = input("1 - take out money\n2 - set money\n3 - update product\n4 - add currency")
        if which_service == "1" and is_access:
            #self.moneyGet(self.getAccessFlag())
            self.access_flag = False
        elif which_service == "2" and is_access:
            plnIn = input("Input pln: ")
            usdIn = input("Input usd: ")
            #self.moneySet(self.getAccessFlag(), plnIn, usdIn)
            self.access_flag = False
        elif which_service == "3" and is_access:
            #self.setProducts(self.getAccessFlag())
            self.access_flag = False
        elif which_service == "4" and is_access:
            #self.setCoefficient(self.getAccessFlag())
            self.access_flag = False
        else:
            print("Access denied.")
