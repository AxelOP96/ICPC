cases = int(input());
count =0;
answer = list();
for x in range(cases):
    distances = list(map(int, input().split()));
    if distances[0] < distances[1]:
        count = count +1;
    if distances[0] < distances[2]:
        count = count +1;
    if distances[0] < distances[3]:
        count = count +1;
    answer.append(count);
    count =0;

for y in range(len(answer)):
    print(answer[y]);
