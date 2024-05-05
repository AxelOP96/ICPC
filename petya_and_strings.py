word1 = input();
word2 = input();
if word1.lower() == word2.lower():
    print(0);
if word1.lower() < word2.lower():
    print(-1);
if word1.lower() > word2.lower():
    print(1);
