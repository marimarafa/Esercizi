# In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento. I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati. Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa, i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

# - Tartaruga:
#     - Passo veloce (50% di probabilità): avanza di 3 quadrati.
#     - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
#     - Passo lento (30% di probabilità): avanza di 1 quadrato.

# - Lepre:
#     - Riposo (20% di probabilità): non si muove.
#     - Grande balzo (20% di probabilità): avanza di 9 quadrati.
#     - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
#     -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
#     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

# Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

# Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole.

# Iniziate la gara stampando:
# 'BANG !!!!! AND THEY'RE OFF !!!!!'

# Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga, la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. Occasionalmente, i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione. Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

# Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. Se è così, stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!". Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

# Requisiti del Codice:
# - Utilizzare il modulo random per la generazione dei numeri casuali.
# - Definire e utilizzare:
#     - una funzione per visualizzare le posizioni sulla corsia di gara,
#     - una funzione per calcolare la mossa della tartaruga,
#     - una funzione per calcolare la mossa della lepre.
# - Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.


import random


print("'BANG !!!!! AND THEY'RE OFF !!!!!'")
turtle_position1 = 1
lepre_position1 = 1

def position():
    position = ["_"] * 70
    turtle_position(turtle_position1)
    lepre_position(lepre_position1)
    for i in position:
        if i == turtle_position1:
            print("T")
        elif i == lepre_position1:
            print("H")
        print(position)
        if turtle_position1 == lepre_position1:
            print("OUCH!!!")
        if turtle_position1 == 70:
            print("TORTOISE WINS! || VAY!!!")
        elif lepre_position1 == 70:
            print("HARE WINS || YUCH!!!")
        elif lepre_position1 == 70 and turtle_position1 == 70:
            print("IT'S A TIE.")

def turtle_position(turtle_position):
    print("La tartarugha ha fatto una :")
    for i in range(random.randint(1,10 +1)):
        if 1 <= i <= 5:
            print("Passo veloce!")
            turtle_position  += 3
        elif 6 <= i <= 7:
            print("Scivolata!")
            turtle_position -= 6
            if i < 0:
                turtle_position == position[0]
        elif 8 <= i <= 10:
            print("Passo lento!")
            turtle_position += 1
    return turtle_position

def lepre_position(lepre_position):
    print("La lepre ha fatto una :")
    for i in range(random.randint(1,10 +1)):
        if 1 <= i <= 2:
            print("Riposo!")
            lepre_position == 0
        elif 3 <= i <= 4 :
            print("Grande balzo!")
            lepre_position += 9
        elif i <= 5:
            print("Grande scivolata!")
            lepre_position -= 12
            if i < 0:
                lepre_position == position[0]
        elif 6 <= i <= 8:
            print("Piccolo balzo!")
            lepre_position += 1
        elif 9 <= i <= 10:
            print("Piccola scivolata!")
            lepre_position -= 2
            if i < 0:
                lepre_position == position[0]
    return lepre_position


position()








        



