import product as p
import random
# from interruptingcow import timeout  # https://pypi.org/project/interruptingcow/
# no signal on win os module 'signal' has no attribute 'SIGALRM'
import timeout
import curr as c
#import exchanger as ex

class Machine:
    def __init__(self):
        # Initialize the new instance
        self.products = {}
        self.currencies = {"usd": c.Currency(4.95)}
        self.money = {"pln": 0, "usd": 0}
        self.accessFlag = False

    def getAccessFlag(self):
        return self.accessFlag

    def setAccessFlag(self, value):
        self.accessFlag = value

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

    ##############################################################################################
    # @ co to, poczytac
    @timeout.timeout(60)
    def serviceTask(cls, accessFlag):
        serwisJob = input("1 - take out money\n2 - set money\n3 - update product\n4 - add currency")
        if serwisJob == "1" and accessFlag:
            cls.moneyGet(cls.getAccessFlag())
            cls.setAccessFlag(False)
        elif serwisJob == "2" and accessFlag:
            plnIn = input("Input pln: ")
            usdIn = input("Input usd: ")
            cls.moneySet(cls.getAccessFlag(), plnIn, usdIn)
            cls.setAccessFlag(False)
        elif serwisJob == "3" and accessFlag:
            cls.setProducts(cls.getAccessFlag())
            cls.setAccessFlag(False)
        elif serwisJob == "4" and accessFlag:
            cls.setCoefficient(cls.getAccessFlag())
            cls.setAccessFlag(False)
        else:
            print("Access denied.")

    def switch(cls, case):
        if case == "serwis":
            x = random.randint(0, 9)
            if input(str(x)) == str(x + 1):
                cls.setAccessFlag(True)
                print("You have 60 sek.\n")
                try:
                    cls.serviceTask(cls.getAccessFlag())
                except:
                    print("Didn't finish within 60 seconds")
                    cls.setAccessFlag(False)
                # try:
                #     with timeout(10):  # stops after 10 sek
                #         serwisJob = input("1 - take out money\n2- set money\n3-update product\n")
                #         if serwisJob == "1":
                #             cls.moneyGet(1)
                #         elif serwisJob == "2":
                #             plnIn = input("Input pln: ")
                #             usdIn = input("Input usd: ")
                #             cls.moneySet(1, plnIn, usdIn)
                #         elif serwisJob == "3":
                #             cls.setProducts(1)
                #         else:
                #             pass
                # except RuntimeError:
                #     print("didn't finish within 10 seconds")  # działa tylko w unix interruptingcow
            else:
                print("Service not granted.\n")
            return 1

        elif case == "stop":
            return "exit"

        elif case == "start":
            iterator = 1
            for k, v in cls.products.items():
                print(str(iterator) + ". " + str(k) + " " + str(v.returnCost()))
                iterator += 1
            coffeeCase = input("Pic up a coffe by a name: ")

            if coffeeCase in cls.products:
                waitConfirmation = False

                while not waitConfirmation:
                    paymentOption = input("Input pln/else/card: ")

                    if paymentOption == "pln":
                        cls.pay("pln", cls.products[coffeeCase].returnCost())
                        print("Pls wait...\nDone.")
                        waitConfirmation = True

                    elif paymentOption == "else":
                        # url = 'https://api.exchangerate-api.com/v4/latest/USD'
                        # converter = ex.RealTimeCurrencyConverter(url)
                        # converted = converter.convert('PLN', 'USD', float(cls.products[coffeeCase].returnCost()))
                        # cls.pay("usd", converted)
                        for currencies in cls.currencies.keys():
                            print(currencies)
                        currency = input("Pick currency: ")
                        converted = float(cls.products[coffeeCase].returnCost()) * cls.currencies[currency].getVal()
                        cls.pay(currency, converted)
                        print("Pls wait...\nDone.")
                        waitConfirmation = True

                    elif paymentOption == "card":
                        cls.pay("pln", cls.products[coffeeCase].returnCost())
                        print("Pls wait...\nDone.")
                        waitConfirmation = True

                    else:
                        inp = input("Invalid payment. Repeat? y/n: ")
                        if inp == "n":
                            waitConfirmation = True
                        else:
                            pass
            else:
                print("Invalid coffee.")
        else:
            print("There is no such option.")
            return 1
