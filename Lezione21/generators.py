def generatore():

    yield "A"
    yield "B"
    yield "C"

prova_generatore = generatore()

print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))

#Context manager con i decorator
import time
from contextlib import contextmanager

@contextmanager
def context_manager_decorator(*args):
    start_time: float = time.time()

    yield

    end_time: float = time.time()
    elapsed_time: float = end_time - start_time

    print(f"{elapsed_time=}")

with context_manager_decorator() as _:
    print("Ciao")