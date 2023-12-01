import fileinput
import re
from collections import deque
from copy import deepcopy

D1 = deque()
D2 = deque()
active_deck = D1

L = list([l.strip() for l in fileinput.input()])
for l in L:
    if 'Player' in l:
        if '2' in l:
            active_deck = D2
    elif l:
        active_deck.append(int(l))

t = 0
def play_game(D1, D2, is_p2):
    SEEN = set()
    while D1 and D2:
        global t
        t += 1
        my_key = (tuple(D1),tuple(D2))
        if my_key in SEEN and is_p2:
            return True,D1
        SEEN.add(my_key)
        c1,c2 = D1.popleft(), D2.popleft()
        if len(D1)>=c1 and len(D2)>=c2 and is_p2:
            NEW_D1 = deque([D1[x] for x in range(c1)])
            NEW_D2 = deque([D2[x] for x in range(c2)])
            p1_wins,_ = play_game(NEW_D1, NEW_D2, is_p2)
        else:
            p1_wins = c1>c2

        if p1_wins:
            D1.append(c1)
            D1.append(c2)
        else:
            D2.append(c2)
            D2.append(c1)
    if D1:
        return True,D1
    else:
        return False,D2

for p2 in [False,True]:
    p1,winner_deck = play_game(deepcopy(D1),deepcopy(D2),p2)
    score = 0
    for i,c in enumerate(winner_deck):
        score += (len(winner_deck)-i)*c
    print(score)
