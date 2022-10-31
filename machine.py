import product as p
import random
# from interruptingcow import timeout  # https://pypi.org/project/interruptingcow/
# no signal on win os module 'signal' has no attribute 'SIGALRM'
import timeout
import exchanger as ex

class Machine:
    def __init__(self):
        # Initialize the new instance
        self.products = {}
        self.money = {"pln": 0, "usd": 0}
        self.accessFlag = False

    def getAccessFlag(self):
        return self.accessFlag

    def setAccessFlag(self, value):
        self.accessFlag = value

    def moneyGet(self, password):
        if password and (self.money["pln"] != 0 or self.money["usd"] != 0):
            print("Withdraw: \nPLN: {}.\nUSD: {}.\n".format(self.money["pln"], self.money["usd"]))
            self.money.update({"pln": 0, "usd": 0})
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
        self.money.update({name: value + self.money[name]})

    def getProducts(self, name): # get product price
        return self.products.get(name)

    def setProducts(self, password): # update or set product
        if password:
            name = input("Input product name: ")
            ingredients = input("Input product ingredients (like *, *): ") # ???
            cost = input("Input product cost: ")
            self.products.update({name: p.Product(ingredients, cost)})
        else:
            print("Access denied.")

    ##############################################################################################
    # @ co to, poczytac
    @timeout.timeout(60)
    def serviceTask(cls, accessFlag):
        serwisJob = input("1 - take out money\n2 - set money\n3 - update product\n")
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
############################################# product
        elif case == "start":
            iterator = 1
            for k in cls.products:
                print(str(iterator) + ". " + str(k) + " " + str(k[1]) + "\n")
                iterator += 1
            coffeeCase = input("Pic up a coffe by a name: ")

            if coffeeCase in cls.products:
                waitConfirmation = False

                while not waitConfirmation:
                    paymentOption = input("Input PLN/USD/CARD: ")
                    if paymentOption == "PLN" or "CARD":
                        cls.pay("pln", cls.products[coffeeCase[1]])
                        waitConfirmation = True
                    elif paymentOption == "USD":
                        url = 'https://api.exchangerate-api.com/v4/latest/USD'
                        converter = ex.RealTimeCurrencyConverter(url)
                        converted = converter.convert('INR', 'USD', cls.products[coffeeCase[1]])
                        cls.pay("usd", converted)
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
