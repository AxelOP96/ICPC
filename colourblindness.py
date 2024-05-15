testCases = int(input());
answer = list();
count =0;
for x in range(testCases):
    columns = int(input());
    colour1 = input();
    colour2 = input();
    for y in range(columns):

        if (colour1[y] == "R" and colour2[y] == "R") or (colour1[y] == "G" and colour2[y] == "G") or (colour1[y] == "G" and colour2[y] == "B") or (colour1[y] == "B" and colour2[y] == "B") or (colour1[y] == "B" and colour2[y] == "G"):
            count = count+1;
    if count == columns:
        answer.append("YES");
    else:
        answer.append("NO");
    count = 0;

for z in range(len(answer)):
    print(answer[z]);
