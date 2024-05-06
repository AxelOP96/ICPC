rooms = int(input());
amountOfRooms =0;
for x in range(rooms):
    peopleAndCapacity = input().split(" ");
    if int(peopleAndCapacity[1]) - int(peopleAndCapacity[0]) >= 2:
        amountOfRooms = amountOfRooms +1;

print(amountOfRooms);
