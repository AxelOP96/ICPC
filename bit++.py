x = int(input());
answer = 0;
for i in range(x):
    ope = input();
    if ope == "X++" or ope == "++X":
        answer = answer+1;
    if ope == "--X" or ope == "X--":
        answer = answer-1;

print(answer);
