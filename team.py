amount = int(input());
interna =0;
externa = 0;
for x in range(amount):
    a, b, c = list(map(int, input().split()));
    if a == 1:
        interna = interna+1;
    if b == 1:
        interna = interna+1;
    if c == 1:
        interna = interna+1;
    if interna >= 2:
        externa = externa+1;
    interna =0;

print(externa);
