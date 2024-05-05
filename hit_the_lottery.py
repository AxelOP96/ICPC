dollars = int(input());
amount =0;
if dollars >= 100:
    while dollars >= 100:
        dollars = dollars-100;
        amount = amount +1;
if dollars>= 20:
    while dollars >= 20:
        dollars = dollars -20;
        amount = amount +1;
if dollars >= 10:
    while dollars >= 10:
        dollars = dollars -10;
        amount = amount +1;

if dollars >= 5:
    while dollars >= 5:
        dollars = dollars -5;
        amount = amount +1;
if dollars >= 1:
    while dollars >= 1:
        dollars = dollars -1;
        amount = amount +1;

print(amount);
