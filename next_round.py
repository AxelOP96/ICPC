participants, place = list(map(int, input().split()));
total =0;
score =0;
scores = list(map(int, input().split()));
zero =0;
for x in range(len(scores)):
    score = scores[place-1];
    if score == 0 and scores[x] == 0:
        zero = zero +1;
    elif score <= scores[x]:
        total = total +1;
if zero != len(scores):
    print(total);
else:
    print(0);
