import machine


def run():

    start = True
    coffee_machine = machine.Machine()

    while start:
        case = input("start/stop/(service +1): ")  # user input of choice

        if case == "service":
            try:
                coffee_machine.service_for_user()  # service task
            except:
                print("Didn't finish within 60 seconds")
                pass

        elif case == "stop":  # end program
            start = False

        elif case == "start":
            coffee_machine.default_task()  # start ordering coffee

        else:
            print("There is no such option.")

    exit(0)
