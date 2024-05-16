testCase = input();
count = 0;
for x in range(len(testCase)):
    if testCase[x] == "4" or testCase[x] == "7":
        count = count+1;

if count == 4 or count ==7 or count == 47 or count == 744 or count == 74:
    print("YES");
else: print("NO");
