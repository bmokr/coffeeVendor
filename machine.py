import product as p
import random
# from interruptingcow import timeout  # https://pypi.org/project/interruptingcow/
# no signal on win os module 'signal' has no attribute 'SIGALRM'
import timeout


class Machine:
    def __init__(self):
        # Initialize the new instance
        self.products = {}
        self.money = {"pln": 0, "usd": 0}

    def moneyGet(self, password) -> object:
        if password & self.money["pln"] != 0 | self.money["usd"] != 0:
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
    def serviceTask(cls):
        serwisJob = input("1 - take out money\n2 - set money\n3 - update product\n")
        if serwisJob == "1":
            cls.moneyGet(True)
        elif serwisJob == "2":
            plnIn = input("Input pln: ")
            usdIn = input("Input usd: ")
            cls.moneySet(True, plnIn, usdIn)
        elif serwisJob == "3":
            cls.setProducts(1)
        else:
            pass

    def switch(cls, case):
        if case == "serwis":
            x = random.randint(0, 9)
            if input(str(x)) == str(x + 1):
                print("You have 10 sek.\n")
                try:
                    cls.serviceTask()
                except:
                    print("didn't finish within 10 seconds")
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
        elif case == "1":
            for k, v in cls.products
            coffeeCase = input("Pic up a coffe: ")
        elif case == "4":
            return "You can become a Blockchain developer."
        elif case == "5":
            return "You can become a mobile app developer"
        else:
            print("There is no such number.")
            return 1