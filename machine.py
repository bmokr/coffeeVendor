import product as p
import random
from interruptingcow import timeout  # https://pypi.org/project/interruptingcow/


class Machine:
    def __init__(self):
        # Initialize the new instance
        self.products = {}
        self.money = {"pln": 0, "usd": 0}

    def money(self, password):
        if password & self.money["pln"] != 0 | self.money["usd"] != 0:
            print("Withdraw: \nPLN: {}.\nUSD: {}.\n".format(self.money["pln"], self.money["usd"]))
            self.money.update({"pln": 0, "usd": 0})
        else:
            if not password:
                print("Access denied.")
            else:
                print("No money.")

    def money(self, password, pln, usd):
        if password:
            self.money.update({"pln": pln, "usd": usd})
            print("Machine deposit is now updated.")
        else:
            print("Access denied.")

    def get_products(self, name):
        return self.products.get(name)

    def set_products(self):
        name = input("Input product name: ")
        ingredients = input("Input product ingredients (like *, *): ")
        cost = input("Input product cost: ")
        self.products.update({name: p.Product(ingredients, cost)})

    ##############################################################################################

    @staticmethod  # co to poczytac
    def switch(case):
        if case == "serwis":
            x = random.randint(0, 9)
            print()
            if input(str(x)) == str(x + 1):
                print("You have 60 sek.\n")
                try:
                    with timeout(60, exception=RuntimeError):  # stops after 60 sek
                        serwisJob = input("1 - take out money")
                except RuntimeError:
                    print
                    "didn't finish within 60 seconds"
            else:
                print("serwis nie zostal przyznany")
            return 1
        elif case == "stop":
            return "exit"
        elif case == "3":
            return "You can become a Data Scientist"
        elif case == "4":
            return "You can become a Blockchain developer."
        elif case == "5":
            return "You can become a mobile app developer"
