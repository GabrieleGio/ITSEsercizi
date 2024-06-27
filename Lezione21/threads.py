#Utilizzo di un thread
# import time
# def funzione(id: int):
#     print(f"{id=} time {time.time()}")
#     time.sleep(1.5)
#     print(f"{id=} time {time.time()}")

# if __name__ == "__main__":

#     import threading

#     x = threading.Thread(target=funzione, args=(1,))
#     print(f"Prima di runnare il thread {time.time()}")
#     x.start()
#     print(f"Ho runnato il thread {time.time()}")
#     x.join()
#     print(f"Ho finito di runnare il thread??? {time.time()}")


import time
import random
def funzione(id: int):
    print(f"{id=} time {time.time()}")
    time.sleep(1.5)
    print(f"{id=} time {time.time()}")

if __name__ == "__main__":

    import threading

    lista_thread = []

    for id in range(3):

        x = threading.Thread(target=funzione, args=(id,))
        lista_thread.append(x)
        print(f"Prima di runnare il thread {time.time()}")
        x.start()
        print(f"Ho runnato il thread {time.time()}")
        x.join()
        print(f"Ho finito di runnare il thread??? {time.time()}")

    for t in lista_thread:
        t.join()
        print(f"Terminato!")





