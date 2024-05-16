integers = list(map(int, input().split()));
#number = integers[0];
for x in range(integers[1]):
    if str(integers[0]).endswith("0"):
        integers[0] = integers[0]//10;
    else:
        integers[0] = integers[0]-1;

print(integers[0]);
