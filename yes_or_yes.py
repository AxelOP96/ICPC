testCases = int(input());
answer = list();
for x in range(testCases):
    word = input().capitalize();
    if word == "Yes":
        answer.append("YES");
    else:
        answer.append("NO");

for y in range(len(answer)):
    print(answer[y]);
