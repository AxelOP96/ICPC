testCases = int(input());
answer = list();
for x in range(testCases):
    a, b, c = list(map(int, input().split()));
    if a + b >= 10 or a + c >= 10 or b +c >= 10:
        answer.append("YES");
    else:
        answer.append("NO");

for y in range(len(answer)):
    print(answer[y]);
