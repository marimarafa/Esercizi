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


def position(turtle_move,hare_move):
    print("'BANG !!!!! AND THEY'RE OFF !!!!!'")
    position = ["-"] * 70
    turtle_position(turtle_move)
    hare_position(hare_move)
    for i in len(position):
        if i == turtle_move:
            i = "T"
        elif i == hare_move:
            i = "H"
        print(position)
    if turtle_move == hare_move:
        i =("OUCH!!!")
    if turtle_move == 70:
        print("TORTOISE WINS! || VAY!!!")
    if hare_move == 70:
        print("HARE WINS || YUCH!!!")
    if hare_move == 70 and turtle_move == 70:
        print("IT'S A TIE.")

def turtle_position(turtle_pos):
    print("La tartaruga:\n")
    i =(random.randint(1,10))
    if 1 <= i <= 5:
        print("Passo veloce!")
        turtle_pos  += 3
    elif 6 <= i <= 7:
        print("Scivolata!")
        turtle_pos -= 6
        if turtle_pos < 0:
            turtle_pos == 0
    elif 8 <= i <= 10:
        print("Passo lento!")
        turtle_pos += 1
    return turtle_pos

def hare_position(hare_pos):
    print("La lepre:\n")
    i = (random.randint(1,10))
    if 1 <= i <= 2:
        print("Riposo!")
        hare_pos == 0
    elif 3 <= i <= 4 :
        print("Grande balzo!")
        hare_pos += 9
    elif i <= 5:
        print("Grande scivolata!")
        hare_pos -= 12
        if hare_pos< 0:
            hare_pos == 0
    elif 6 <= i <= 8:
        print("Piccolo balzo!")
        hare_pos += 1
    elif 9 <= i <= 10:
        print("Piccola scivolata!")
        hare_pos -= 2
        if hare_pos < 0:
            hare_pos == 0
    return hare_pos


turtle_position1 = 1
hare_position1 = 1

position(turtle_position1,hare_position1)








        




