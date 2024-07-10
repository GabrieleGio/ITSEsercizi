from multiprocessing import Process
from bubblesort import bubble_sort_v2
import time

def sleep():
    print(f"Sono nella funzione")
    time.sleep(60)
    print(f"Sto uscendo dalla funzione")

if __name__ == '__main__':

    tic:float = time.time()
    t1 = Process(target=sleep)
    t2 = Process(target=sleep)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    toc:float = time.time()
    time_elapsed:float = toc - tic

    print(f"{time_elapsed=}")

#def parent():