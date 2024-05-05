s = input()
t = input()

word = "";
index = len(t);
if len(s) == len(t):
    for x in range(len(t)):
        if t[x] == s[index-1]:
            word += s[index-1];
            index = index-1;
    if word == t:
        print("YES");
    else:
        print("NO");
else:
    print("NO");
