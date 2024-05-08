amount = int(input());
initial = 0;
less = 0;
more = 0;
answer =0;
lista = list(map(int, input().split()));

for x in range(len(lista)):
    if x ==0:
        initial = lista[0];
        less = initial;
    elif lista[x] > initial:
        answer = answer+1;
        initial = lista[x];
    elif lista[x] < less:
        answer = answer+1;
        less = lista[x]

print(answer);
