s = input();
amountL =0;
amountU =0;

for x in range(len(s)):
    if s[x].islower():
        amountL = amountL +1;
    if s[x].isupper():
        amountU = amountU +1;

if amountL >= amountU:
    print(s.lower());
else:
    print(s.upper());
