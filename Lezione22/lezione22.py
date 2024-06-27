
class Analisi:

    @staticmethod
    def tempo(func):
        def wrapper(*args):
            import time

            start = time.time()
            func(*args)
            print(f"Time elapsed: {time.time() - start}")
        return wrapper

@Analisi.tempo
def area_cerchio(raggio:float):
    return raggio * raggio * 3.14

area_cerchio(1)


def generatore():
    yield "A"
    yield "B"
    yield "C"

prove_generatore = generatore()
print(next(prove_generatore))
print(next(prove_generatore))
print(next(prove_generatore))

from contextlib import contextmanager

@contextmanager
def context_manager_decorator(*args):
    import time
    start_time :float = time.time()
    yield
    end_time :float = time.time()
    elapsed_time = end_time - start_time

    print(f'Elaspsed time: {elapsed_time}')

@context_manager_decorator
def area_cerchio(raggio:float):
    return raggio * raggio * 3.14

area_cerchio(1)

import sys
 
a = []
b = a 
print(sys.getrefcount(a))
print(sys.getrefcount(b))

