testCases = int(input());
answer = list();
for x in range(testCases):
    lista = list(map(int, input().split()));
    if int(lista[0]) + int(lista[1]) == int(lista[2]):
        answer.append("+");
    else:
        answer.append("-");

for y in range(len(answer)):
    print(answer[y]);
