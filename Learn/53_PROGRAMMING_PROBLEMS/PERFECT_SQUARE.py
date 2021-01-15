l = list()
while True:
    n = int(input("Digite outro valor inteiro entre (-10000<=N<=10000): "))
    l.append(n)
    if n == 0:
        break
for i in l:
    if i == 0:
        break
            
    for k in range(0, abs(i)+1):
        if k*k == abs(i) and abs(i) != 1:
            print(i)