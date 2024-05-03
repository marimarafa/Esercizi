#marim arafa
#2-5-2024
"""
Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
"""
def countdown(n: int) -> int:
    for num in range(n,0 -1,-1):
        print(num)
countdown(5)
print("\n")

"""
Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". Un numero magico è definito come un numero che contiene il numero 7
"""
def is_magic_number(num: int) -> bool:
    if "7" in str(num):
            return True
    return False
print(is_magic_number(str(347)))
print("\n")

"""
Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
"""
def list_statistics(numbers: list[int]) -> float :
    return min(numbers),max(numbers),sum(numbers) / len(numbers)
print(list_statistics([1,2,3,4,5]))
print("\n")

"""
Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.
"""
# def rounded_average(numbers: list[int]) -> int:
#     for num in numbers:
#          return 
    
"""
Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo se il 
nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".
"""
def check_access(username: str, password: str, is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True :
          return "Accesso consentito"
    else:
          return "Accesso negato"
print(check_access("lara","12345",True))
print("\n")

"""
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi
che chiude.
"""
def check_parentheses(expression: str) -> bool:
    return expression.count("(") == expression.count(")") and expression[0] == "(" and expression[-1] == ")"
         
print(check_parentheses(")("))
print("\n")
"""
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
"""
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    for num in elements_to_remove:
            if num in original_set:
                original_set.remove(num)
    return original_set 
print(remove_elements({2,13,4,5,6},[2,4,5]))
print("\n")

"""
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.
"""
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    merged_dict = {}
    for key in dict1:
        if key in dict2:
            merged_dict[key] = dict1[key] + dict2[key]
        else:
            merged_dict[key] = dict1[key]
    for key in dict2:
        if key not in dict1:
            merged_dict[key] = dict2[key]
    return merged_dict
print(merge_dictionaries({},{"h":3,"b":5}))
print("\n")

"""
Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.
"""
def rounded_average(numbers: list[int]) -> int:
    media = sum(numbers)/len(numbers)
    return round(media)
print(rounded_average([1,2,3,4,5]))
print("\n")

"""
Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se non è
 affiancato sia a destra che a sinistra da elementi uguali.
"""
def count_isolated(list_num :list) -> int:
    count = 0
    for i in range(len(list_num)):
        if i == 0 and list_num[i] != list_num[i + 1]:
            count += 1
        elif i == len(list_num) - 1 and list_num[i] != list_num[i - 1]:
            count += 1
        elif list_num[i] != list_num[i - 1] and list_num[i] != list_num[i + 1]:
            count += 1
    return count
print(count_isolated([1,2,3,4,4,5]))
print("\n")

"""
Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. La rotazione verso sinistra significa che ciascun
 elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo 
 slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.
"""
def rotate_left(elements: list, k: int) -> list:
    n = 0
    for num in range (len(elements)):
        if elements[n]:
            elements[n -k]
    return elements
print(rotate_left([2,3,4,8],1))
#def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
