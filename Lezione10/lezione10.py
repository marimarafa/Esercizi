#marim arafa  22-05-2024
"""
Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1."""
def transform(x: int) -> int:
    if x % 2 == 0:
        x = x//2
    else:
        x = x *3 -1
    return x

print(transform(4))
print(transform(-10),"\n")

"""
Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. L'azienda paga 10 dollari all'ora per le prime 40 ore di 
lavoro e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo
"""
def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        stipendio = ore_lavorate * 10 
        return float(stipendio)
    if ore_lavorate > 40:
        stipendio = ore_lavorate * 15
        return float(stipendio)

print(calcola_stipendio(40))
print(calcola_stipendio(0))
print(calcola_stipendio(60),"\n")


def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1,8):
        print(i)

    print("Sequenza b):")
    for i in range(3,24,5):
        print(i)

    print("Sequenza c):")
    for i in range(20, -11,-6):
        print(i)
    print("Sequenza d):")
    for i in range(19,52,8):
        print(i)
    return(i)

print_seq()
print("\n")

"""
Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
"""
def countdown(n: int) -> int:
    for _ in range(n):
        print(n)
        n -= 1
    return n
print(countdown(5))

"""Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent. 
Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!
"""
