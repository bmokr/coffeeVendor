import traceback
import machine as m


def run():
    start = True # kondycja głównej pętli

    try:    # dodanie maszyny
        coffeMachine = m.Machine()
    except:
        print(traceback.format_exc())

    while start:
        switch = input("Wybierz numer: ")
        state = coffeMachine.switch(switch)
        if state == "exit":
            start = False
        else:
            pass

    exit(0)
