amount = int(input());

for i in range(amount):
    word = input();
    if len(word) > 10:
        start = word[0];
        end = word[len(word)-1];
        print(start+ str(len(word)-2) +end);
    else:
        print(word);
