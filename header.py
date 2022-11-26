import machine
import random


def run():
    start = True
    coffee_machine = machine.Machine()

    while start:
        case = input("start/stop/(service +1): ")  # user input of choice

        if case == "service":
            password = random.randint(0, 9)  # generate password - simplest method
            if input(str(password)) == str(password + 1):
                print("You have 60 sek.\n")
                coffee_machine.access_flag = True  # granting access
                try:
                    coffee_machine.service_task(coffee_machine.access_flag())
                except:
                    print("Didn't finish within 60 seconds")
                    coffee_machine.access_flag = False  # removing access
            else:
                print("Service not granted.\n")

        elif case == "stop":
            start = False

        elif case == "start":
            iterator = 1
            ###################################################################
            for k, v in cls.products.items():
                print(str(iterator) + ". " + str(k) + " " + str(v.returnCost()))
                iterator += 1
            coffeeCase = input("Pic up a coffee by a name: ")

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
            pass

    exit(0)
