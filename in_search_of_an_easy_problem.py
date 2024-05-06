amount = int(input())

inp = input().split(" ");
answer = "EASY";
for x in range(len(inp)):
    if int(inp[x]) == 1:
        answer = "HARD"
        break;

print(answer);
