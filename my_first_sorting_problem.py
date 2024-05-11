testCases = int(input());
answer = [];
for x in range(testCases):
    integers = list(map(int, input().split()));
    if integers[0] <= integers[1]:
        min = integers[0];
        max = integers[1];
        ord = (min, max)
        answer.append(ord);
    else:
        min = integers[1];
        max = integers[0];
        ord = (min, max)
        answer.append(ord);

for ord in answer:
    print(ord[0],ord[1])
