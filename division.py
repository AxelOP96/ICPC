limit = int(input());

for i in range(limit):
    num = int(input());
    if num >= 1900:
        print("Division 1");
    if num >= 1600 and num <= 1899:
        print("Division 2");
    if num >= 1400 and num <= 1599:
        print("Division 3");
    if num <= 1399:
        print("Division 4");
