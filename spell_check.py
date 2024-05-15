testCases =int(input());
answer = list();
checklist = ["T", "i", "m", "u", "r"];
comparator = set();
for x in range(testCases):
    length = int(input());
    name = input();
    if length == 5:
        for y in range(len(checklist)):
            if name[y] == checklist[0] or name[y] == checklist[1] or name[y] == checklist[2] or name[y] == checklist[3] or name[y] == checklist[4]:
                comparator.add(name[y]);
        if len(comparator) == length:
            answer.append("YES");
        else:
            answer.append("NO");
        comparator.clear();
    else:
        answer.append("NO");

for z in range(len(answer)):
    print(answer[z]);
