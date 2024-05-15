testCases = int(input());
answer = list();
rows = 8;
columns = 8;
for x in range(testCases):
    word ="";
    for y in range(columns):
        line = input()
        for z in range(rows):
            if line[z] != ".":
                word = word + line[z];
    answer.append(word);

for i in range(len(answer)):
    print(answer[i]);
