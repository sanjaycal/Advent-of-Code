f = open("202022a.txt","r")
f = f.read()
f = f.split("\n")
p1 = []

for i in f:
    p1.append(int(i))


f = open("202022b.txt","r")
f = f.read()
f = f.split("\n")
p2 = []

for i in f:
    p2.append(int(i))


import math


print(p1)
print(p2)
Turns = []


def recursive_combat(deck1, deck2):
    previous_games = set()
 
    player1 = deck1.copy()
    player2 = deck2.copy()
 
    winner = None
    while not winner:
        if (tuple(player1), tuple(player2)) in previous_games:
            winner = "p1"
        else:
            previous_games.add((tuple(player1), tuple(player2)))
 
            card1 = player1.pop(0)
            card2 = player2.pop(0)
 
            if card1 <= len(player1) and card2 <= len(player2):
                result = recursive_combat(player1[:card1], player2[:card2])[0]
 
                if result == "p1":
                    player1.append(card1)
                    player1.append(card2)
                else:
                    player2.append(card2)
                    player2.append(card1)
            else:
                if card1 > card2:
                    player1.append(card1)
                    player1.append(card2)
                else:
                    player2.append(card2)
                    player2.append(card1)
 
            if len(player1) == 0:
                winner = "p2"
            elif len(player2) == 0:
                winner = "p1"
 
    return winner, player1, player2


def part2(player1, player2):
    result = recursive_combat(player1, player2)
    if result[0] == "p1":
        winner = result[1]
    else:
        winner = result[2]
 
    t = 0
    print(winner)
    c = 1
    t = 0
    winner.reverse()
    for i in winner:
        t+=c*i
        c+=1
 
    print(t)

part2(p1,p2)




