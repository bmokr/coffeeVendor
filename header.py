import traceback
import machine as m


def run():
    start = True
    try:
        coffeMachine = m.Machine()
    except:
        print(traceback.format_exc())

    while start:
        switch = input("start/stop: ")
        state = coffeMachine.switch(switch)
        if state == "exit":
            start = False
        else:
            pass

    exit(0)
