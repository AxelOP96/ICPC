testCases = int(input());
answer = list();
word = "codeforces";

for x in range(testCases):
    count =0;
    wordCase = input();
    for y in range(len(word)):
        if wordCase[y] != word[y]:
            count = count +1;
    answer.append(count);

for z in range(len(answer)):
    print(answer[z]);
