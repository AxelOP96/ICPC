
word = input();
newWord = "";
for i in range(len(word)):
    if word[i].upper() != "A" and word[i].upper() != "E" and word[i].upper() != "I" and word[i].upper() != "O" and word[i].upper() != "U" and word[i].upper() != "Y":
        newWord += "." + word[i].lower();

print(newWord);
