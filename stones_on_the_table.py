amount = int(input());

text = input();
aux = text[0];
contador =0;
for x in range(1, len(text)):
    if aux == text[x]:
        contador = contador+1;
    aux = text[x]

print(contador);
