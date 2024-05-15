testCases = int(input());
answer = list();
for x in range(testCases):
    countA =0;
    countB =0;
    letters = input();
    for y in range(len(letters)):
        if letters[y] == "A":
            countA = countA +1;
        elif letters[y] == "B":
            countB = countB +1;
    if countA >countB:
        answer.append("A");
    elif countB > countA:
        answer.append("B");

for z in range(len(answer)):
    print(answer[z]);
