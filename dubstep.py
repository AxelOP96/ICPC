word = input().split("WUB");

for x in range(len(word)-1, 0, -1):
    if word[x] == "":
        word.remove(word[x]);


if len(word) > 1:
    print((" ").join(word));
else:
    print(word[0]);
