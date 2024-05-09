cases = int(input());

first = 0;
second =0;
answer = list();
for x in range(cases):
    num = input();
    first += int(num[0]) + int(num[1]) + int(num[2]);
    second += int(num[3]) + int(num[4]) + int(num[5]);
    if first == second:
        answer.append("YES");
    else:
        answer.append("NO");
    first =0;
    second =0;

for y in range(len(answer)):
    print(answer[y]);
