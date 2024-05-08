word = input();
countTodas =0;
for x in range(len(word)):
    if word[x].isupper():
        countTodas = countTodas +1;

if countTodas == len(word):
    print(word.lower());
elif word[0].islower() and countTodas == len(word)-1:
    print(word.capitalize());
else:
    print(word);
