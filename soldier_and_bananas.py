#bear_limak, bear_bob = [x for x in map(int,input().split())];

costOfBanana, amountDollars, amountBananas = [x for x in map(int,input().split())];
amountBorrowed = 0;
total =0;
for i in range(1,amountBananas+1):
    total += i * costOfBanana;

amountBorrowed = total - amountDollars;
print(amountBorrowed);
