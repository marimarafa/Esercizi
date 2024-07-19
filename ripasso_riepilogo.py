#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for key in dict1:
        for key2 in dict2:
            if key == key2:
                result = dict1[key] + dict2[key2]
                dict1 = {key:result}
    return dict1

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

# Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se 
# entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA is True or (conditionB and conditionC) is True:
        return 'Operazione permessa'
    else:
        return 'Operazione negata'

print(check_combination(True, False, True))
print(check_combination(False, True, False))

#Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

def sum_above_threshold(numbers: list[int], x:int) -> int:
    lista = []
    for num in numbers:
        if x <= num:
            lista.append(num)
            return sum(lista)

	
print(sum_above_threshold([15, 5, 25], 20))

# Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
# a) 1, 2, 3, 4, 5, 6, 7
# b) 3, 8, 13, 18, 23
# c) 20, 14, 8, 2, -4, -10
# d) 19, 27, 35, 43, 51

def print_seq(): 
    
    print("Sequenza a):")
    for num in range(1,8):
        print(num)

    print("Sequenza b):")
    for num in range(3,24,5):
        print(num)

    print("Sequenza c):")
    for num in range(20,-11,-6):
        print(num)

    print("Sequenza d):")
    for num in range(19,52,8):
        print(num)
    
print_seq()
#Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    new_dict = {}
    for key,value in prodotti.items():
        if value > 20:
            new_dict[key] = value - (value * 0.1)
    return new_dict

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
