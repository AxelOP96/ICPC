distance = int(input());
steps = 0;
for i in range(distance):
    if distance > 5:
        distance-=5;
        steps+=1;


steps+=1;
print(steps);
