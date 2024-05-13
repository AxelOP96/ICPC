testCases = int(input());
answer = list();
for x in range(testCases):
    cards = input();
    if cards[0] == "a" and cards[1] == "b" and cards[2] == "c":
        answer.append("YES");
    elif cards[0] == "a" and cards[1] == "c" and cards[2] == "b":
        answer.append("YES");
    elif cards[0] == "b" and cards[1] == "a" and cards[2] == "c":
        answer.append("YES");
    elif cards[0] == "c" and cards[1] == "b" and cards[2] == "a":
        answer.append("YES");
    else:
        answer.append("NO");

for y in range(len(answer)):
    print(answer[y])
