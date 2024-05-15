testCases = int(input());
answer = list();
for x in range(testCases):
    digits = list(map(int, input().split()));
    if digits[0] < digits[1] and digits[1] < digits[2] and digits[0] < digits[2]:
        answer.append("STAIR");
    elif digits[0] < digits[1] and digits[2] < digits[1]:
        answer.append("PEAK");
    else:
        answer.append("NONE");

for y in range(len(answer)):
    print(answer[y]);
