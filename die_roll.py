yakko, wakko = [x for x in map(int,input().split())];

mayor = max(yakko, wakko);

if mayor == 6:
    print("1/6");
if mayor == 5:
    print("1/3");
if mayor == 4:
    print("1/2");
if mayor == 3:
    print("2/3");
if mayor == 2:
    print("5/6");
if mayor == 1:
    print("1/1");
