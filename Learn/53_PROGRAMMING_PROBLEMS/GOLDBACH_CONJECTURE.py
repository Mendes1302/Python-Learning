N = int(input("Digite um valor entre (2<=N<=4294967294):  "))
l = [2]
count = value = 0
for i in range(1, N+1, 2):
    for k in range(N, 0, -1):
        if i >= k and i%k == 0:
            count += 1
        if count == 2 and k == 1:
            l.append(i)
        if count > 2:
            break
    count = 0

for i in l:
    for k in range(len(l)-1, -1, -1):
        if l[k] + i == N:
            value = 1
            print(f"{i} + {l[k]} = {N}")
            break
    if value:
        break