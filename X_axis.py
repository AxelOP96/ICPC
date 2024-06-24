testCases = int(input());

answer = list();
for x in range(testCases):
    integers = list(map(int, input().split()));
    a = 0;
    x1 = integers[0];
    x2 = integers[1];
    x3 = integers[2];
    op1 = (x1 - x2)
    op2 = (x2 - x2)
    op3 = (x3 -x2)
    if  op1 < 0:
        op1 = op1 * -1
    if  op2 < 0:
        op2 = op2 * -1
    if  op3 < 0:
        op3 = op3 * -1
    total = op1 + op2 +op3;
    x1 = integers[1];
    x2 = integers[2];
    x3 = integers[0];
    op1 = (x1 - x2)
    op2 = (x2 - x2)
    op3 = (x3 -x2)
    if  op1 < 0:
        op1 = op1 * -1
    if  op2 < 0:
        op2 = op2 * -1
    if  op3 < 0:
        op3 = op3 * -1
    total2 = op1 + op2 +op3;
    x1 = integers[2];
    x2 = integers[0];
    x3 = integers[1];
    op1 = (x1 - x2)
    op2 = (x2 - x2)
    op3 = (x3 -x2)
    if  op1 < 0:
        op1 = op1 * -1
    if  op2 < 0:
        op2 = op2 * -1
    if  op3 < 0:
        op3 = op3 * -1
    total3 = op1 + op2 +op3;
    a = min(total, total2, total3);
    answer.append(a);

for y in range(len(answer)):
    print(answer[y]);
