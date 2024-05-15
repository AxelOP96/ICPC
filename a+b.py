testCases = int(input());
answer = list();
for x in range(testCases):
    operation = list(map(int, input().split("+")))
    total = operation[0] + operation[1];
    answer.append(total);

for y in range(len(answer)):
    print(answer[y]);
