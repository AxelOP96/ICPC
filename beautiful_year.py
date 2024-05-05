initYear = input();
year = int(initYear);
initial = year;
answer =0;

found = 10000;
while year < found or year == answer+1:
    initYear = str(year);
    if initYear[0] != initYear[1] and initYear[0] != initYear[2] and initYear[0] != initYear[3] and initYear[1] != initYear[2] and initYear[1] != initYear[3] and initYear[2] != initYear[3] and year != initial:
        answer = year;
        break;
    year = year +1;

print(answer);
