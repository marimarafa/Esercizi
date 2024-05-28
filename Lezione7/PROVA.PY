import random

def display_positions(turtle_pos, hare_pos):
    track = ['_'] * 70
    if turtle_pos == hare_pos:
        track[turtle_pos - 1] = 'OUCH!!!'
    else:
        track[turtle_pos - 1] = 'T'
        track[hare_pos - 1] = 'H'
    print(''.join(track))

def move_turtle(turtle_pos):
    move = random.randint(1, 10)
    if 1 <= move <= 5:
        turtle_pos += 3  # Fast plod
    elif 6 <= move <= 7:
        turtle_pos -= 6  # Slip
    else:
        turtle_pos += 1  # Slow plod
    if turtle_pos < 1:
        turtle_pos = 1
    return turtle_pos

def move_hare(hare_pos):
    move = random.randint(1, 10)
    if 1 <= move <= 2:
        pass  # Sleep
    elif 3 <= move <= 4:
        hare_pos += 9  # Big hop
    elif move == 5:
        hare_pos -= 12  # Big slip
    elif 6 <= move <= 8:
        hare_pos += 1  # Small hop
    else:
        hare_pos -= 2  # Small slip
    if hare_pos < 1:
        hare_pos = 1
    return hare_pos

def main():
    print('BANG !!!!! AND THEY\'RE OFF !!!!!')
    turtle_pos = 1
    hare_pos = 1
    while turtle_pos < 70 and hare_pos < 70:
        turtle_pos = move_turtle(turtle_pos)
        hare_pos = move_hare(hare_pos)
        display_positions(turtle_pos, hare_pos)
        if turtle_pos >= 70 and hare_pos >= 70:
            print("IT'S A TIE.")
            break
        elif turtle_pos >= 70:
            print("TORTOISE WINS! || VAY!!!")
            break
        elif hare_pos >= 70:
            print("HARE WINS || YUCH!!!")
            break

if __name__ == "__main__":
    main()
