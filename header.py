import traceback
import machine as m
def run():
    start = True # kondycja głównej pętli

    try:    # dodanie maszyny
        coffeMachine = m.Machine()
        # coffeMachine.set_products()
        # zamienić na wczytanie pliku print(str(coffeMachine.get_products(input("Input name of product: "))))

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
