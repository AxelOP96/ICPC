name = input();
answer = set()
for x in range(len(name)):
    answer.add(name[x]);

if len(answer) %2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
