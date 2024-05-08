cases = int(input());
answer = list();
for x in range(cases):
    lista = list(map(int, input().split()));
    a = lista[0];
    b = lista[1];
    c = lista[2];
    if (a + b ) == c or (a + c) == b or (c+b)==a:
        answer.append("YES");
    else:
        answer.append("NO");

for y in range(len(answer)):
    print(answer[y]);
