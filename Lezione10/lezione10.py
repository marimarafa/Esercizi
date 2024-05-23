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
    else:
        ore_straordinarie = ore_lavorate - 40
        stipendio = 40 * 10 + ore_straordinarie * 15
    return float(stipendio)

print(calcola_stipendio(40))
print(calcola_stipendio(0))
print(calcola_stipendio(60),"\n")

"""Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51
"""
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
print(countdown(5),"\n")

"""Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent. 
Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!
"""
def integerPower(base:int,esponente:int) -> int:
    risultato = 1
    for _ in range(esponente):
        risultato *= base
    return risultato

print(integerPower(3, 4))
print(integerPower(2, 5), "\n")

"""Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. La funzione deve ricevere 
due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.
Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora
"""
def hypotenuse(lenght:float,widht:float)->float:
    # c=√(a2+b2)
    len_hypotenuse =((lenght **2) + (widht **2)) ** 0.5
    return len_hypotenuse
print(hypotenuse(3.0,4.0),"\n")

    
    
