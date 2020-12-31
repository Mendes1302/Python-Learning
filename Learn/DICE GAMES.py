from random import randint
from operator import itemgetter

play = dict()
count = 0

print("Valores sorteados:")
for i in range(0, 4):
    play[f"player{i+1}"] = int(randint(1, 6))

for j,k in play.items():
    print(f"    O {j} tirou {k}")
print()
print("Ranking dos jogadores:")

for l, a in enumerate(sorted(play.items(), key=itemgetter(1))):
    print(f"    {l+1} lugar: {a[0]} com {a[1]}")
