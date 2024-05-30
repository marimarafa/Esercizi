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
# SFIDE AGGIUNTIVE:
# 1. Variabilità Ambientale:
# Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
# Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.

# Modificatori mossa:
# - La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
# - La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.
# 2. Energia o Stamina:
# Aggiungere una metrica di "energia" o "stamina" che diminuisce con ogni movimento e si ricarica in specifiche condizioni. Fare in modo che le mosse che consumano più energia non possano essere eseguite se l'animale non ha abbastanza energia. L'energia inziale per entrambi gli animali è 100.

# Nuove regole di movimento:
# - Tartaruga:
#     - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia, essa guadagna 10 di energia. Non può superare l'energia iniziale.
#     - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
#     - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
#     - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.
# - Lepre:
#     - Riposo (20% di probabilità): non si muove e recupera 10 di energia. Non può superare l'energia iniziale.
#     - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
#     - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia. Non può andare sotto il quadrato 1.
#     - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
#     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia. Non può andare sotto il quadrato 1.

import random

def position(turtle_pos, hare_pos,meteo):
    print("'BANG !!!!! AND THEY'RE OFF !!!!!'")
    tick = 0
    turtle_energy = 100
    hare_energy = 100
    while turtle_pos < 70 and hare_pos < 70:
        turtle_pos,turtle_energy = turtle_position(turtle_pos,turtle_energy,meteo)
        hare_pos,hare_energy = hare_position(hare_pos,hare_energy,meteo)
        tick += 1
        if tick % 10 == 0:
            if meteo == 'soleggiato':
                meteo = 'pioggia'
            else:
                meteo = 'soleggiato'
            print(f"Weather changed to: {meteo}")
        positions = ['-'] * 70
        if turtle_pos == hare_pos:
            positions[turtle_pos - 1] = 'OUCH!!!'
        else:
                positions[turtle_pos - 1] = 'T'
                positions[hare_pos - 1] = 'H'
                
        print(''.join(positions))

        if turtle_pos == 70 and hare_pos == 70:
            print("IT'S A TIE.")
            break
        elif turtle_pos == 70:
            print("TORTOISE WINS! || VAY!!!")
            break
        elif hare_pos == 70:
            print("HARE WINS || YUCH!!!")
            break

def turtle_position(turtle_move, turtle_energy, meteo):
    print("La tartaruga:\n")
    i = random.randint(1, 10)
    if 1 <= i <= 5:
        if turtle_energy >= 5:
            print("Passo veloce!")
            turtle_move += 3
            turtle_energy -= 5
        else:
            print("Non abbastanza energia per Passo veloce.")
            turtle_energy += 10
    elif 6 <= i <= 7:
        if turtle_energy >= 10:
            print("Scivolata!")
            turtle_move -= 6
            turtle_energy -= 10
            if turtle_move < 1:
                turtle_move = 1
        else:
            print("Non abbastanza energia per Scivolata.")
            turtle_energy += 10
    else:
        if turtle_energy >= 3:
            print("Passo lento!")
            turtle_move += 1
            turtle_energy -= 3
        else:
            print("Non abbastanza energia per Passo lento.")
            turtle_energy += 10

    if meteo == "pioggia":
        turtle_move -= 1

    if turtle_move < 1:
        turtle_move = 1
    if turtle_move > 70:
        turtle_move = 70

    print(f'Energia della tartaruga: {turtle_energy}')
    return turtle_move, turtle_energy

def hare_position(hare_move, hare_energy, meteo):
    print("La lepre:\n")
    i = random.randint(1, 10)
    if 1 <= i <= 2:
        print("Riposo!")
        hare_energy += 10
        if hare_energy > 100:
            hare_energy = 100
    elif 3 <= i <= 4:
        if hare_energy >= 15:
            print("Grande balzo!")
            hare_move += 9
            hare_energy -= 15
        else:
            print("Non abbastanza energia per grande balzo.")
    elif i == 5:
        if hare_energy >= 20:
            print("Grande scivolata!")
            hare_move -= 12
            hare_energy -= 20
            if hare_move < 1:
                hare_move = 1
        else:
            print("Non abbastanza energia per grande scivolata.")
    elif 6 <= i <= 8:
        if hare_energy >= 5:
            print("Piccolo balzo!")
            hare_move += 1
            hare_energy -= 5
        else:
            print("Non abbastanza energia per piccolo balzo.")
    else:
        if hare_energy >= 8:
            print("Piccola scivolata!")
            hare_move -= 2
            hare_energy -= 8
            if hare_move < 1:
                hare_move = 1
        else:
            print("Non abbastanza energia per piccola scivolata.")
    if meteo == "pioggia":
        hare_move -= 2
    if hare_move < 1:
        hare_move = 1
    if hare_move > 70:
        hare_move = 70

    print(f'Energia della lepre: {hare_energy}')
    return hare_move, hare_energy


turtle_position1 = 1
hare_position1 = 1
meteo = "soleggiato"

position(turtle_position1,hare_position1,meteo)













