
#from ..Lezione20.decorators import decorator



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
    