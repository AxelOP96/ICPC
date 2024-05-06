longitud = int(input());
winsA =0;
winsD =0;

results = input();
for x in range(longitud):
    if results[x] == "A":
        winsA=winsA+1;
    if results[x] == "D":
        winsD=winsD+1;

if winsA > winsD:
    print("Anton");
if winsD > winsA:
    print("Danik");
if winsD == winsA:
    print("Friendship");
