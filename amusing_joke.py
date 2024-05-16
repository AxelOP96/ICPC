guest = input();
residenceHost = input();
letters = input();

pile = sorted(guest + residenceHost);
lettersSorted = sorted(letters);
count =0;
if (len(pile) != len(lettersSorted)):
    print("NO");
else:
    for x in range(len(pile)):
        if pile[x] != lettersSorted[x]:
            print("NO");
            break;
        else:
            count = count +1;
if count == len(pile):
    print("YES");
