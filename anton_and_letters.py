antonSet = input().replace("{","").replace("}","").replace(",", "").split();
conjunto = set();
for x in antonSet:
    conjunto.add(x);

print(len(conjunto));
