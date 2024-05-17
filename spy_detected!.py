testCases = int(input());
answer = list();
spy = 0
for x in range(testCases):
    length = int(input());
    integers = list(map(int, input().split()));
    for y in range(length):
        if integers.count(integers[y]) == 1:
            answer.append(y+1)

for z in range(len(answer)):
    print(answer[z]);
