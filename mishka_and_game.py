rounds = int(input());
mishkaR = 0;
chrisR =0;
for x in range(rounds):
    x, y = list(map(int, input().split()));
    if x < y:
        chrisR = chrisR +1;
    elif y < x:
        mishkaR = mishkaR +1;

if chrisR < mishkaR:
    print("Mishka");
elif mishkaR < chrisR:
    print("Chris");
else:
    print("Friendship is magic!^^");
