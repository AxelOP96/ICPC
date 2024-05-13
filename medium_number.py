testCases = int(input());
answer = list();
for x in range(testCases):
    a, b, c = list(map(int, input().split()));
    min_value = min(a, b, c)
    max_value = max(a, b, c)
    if a != min_value and a != max_value:
        answer.append(a);
    elif b != min_value and b != max_value:
        answer.append(b);
    else:
        answer.append(c);

for y in range(len(answer)):
    print(answer[y]);
